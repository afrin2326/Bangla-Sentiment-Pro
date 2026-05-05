from fastapi import FastAPI
import torch
import joblib
from transformers import AutoTokenizer
from src.model.architecture import BanglaSentimentEmotionModel
from src.utils.helpers import save_to_db # Importing the database helper function

app = FastAPI()

# --- SETUP COMPUTATION DEVICE ---
# Uses GPU (CUDA) if available, otherwise defaults to CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --- LOAD NLP COMPONENTS ---
# Load the pre-trained BanglaBERT tokenizer from BUET's repository
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglabert")

# Initialize the Custom Dual-Head Model Architecture
# 5 output classes for Sentiment, 7 for Emotion
model = BanglaSentimentEmotionModel(num_sentiments=5, num_emotions=7)

# Load my fine-tuned model weights (.pt file)
# strict=False ensures that minor layer mismatches (like pooler) don't crash the app
model.load_state_dict(
    torch.load("./models/model_state.pt", map_location=device), 
    strict=False
)
model.to(device).eval() # Set model to evaluation mode

# --- LOAD LABEL ENCODERS ---
# These encoders convert numerical predictions back into human-readable strings (e.g., 1 -> 'Happy')
s_le = joblib.load("./models/sentiment_encoder.pkl")
e_le = joblib.load("./models/emotion_encoder.pkl")

@app.get("/")
async def root():
    """Health check endpoint to verify API status."""
    return {"status": "Online", "message": "Bangla Sentiment & Emotion API is ready!"}

@app.post("/predict")
async def predict(data: dict):
    """
    Main prediction endpoint.
    1. Receives Bengali text.
    2. Runs inference through BanglaBERT.
    3. Saves results to MySQL database.
    4. Returns prediction to the user.
    """
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}

    # --- PREPROCESSING ---
    # Convert raw text into tokens that the model understands
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128).to(device)
    
    # --- INFERENCE ---
    with torch.no_grad():
        # Getting logits (raw scores) for both Sentiment and Emotion heads
        s_logits, e_logits = model(inputs['input_ids'], inputs['attention_mask'])
    
    # --- POST-PROCESSING ---
    # Find the index with the highest score
    s_idx = torch.argmax(s_logits).item()
    e_idx = torch.argmax(e_logits).item()
    
    # Convert index to actual label name (e.g., 'Positive', 'Anger')
    s_label = s_le.inverse_transform([s_idx])[0]
    e_label = e_le.inverse_transform([e_idx])[0]
    
    # --- DATABASE INTEGRATION ---
    # Automatically save the record for Business Intelligence/Trend Analysis
    try:
        save_to_db(text, s_label, e_label)
    except Exception as db_error:
        print(f"Warning: Could not save to Database. Error: {db_error}")
        # We continue even if DB fails so the user still gets their result
    
    # Return the final JSON response
    return {
        "text": text,
        "sentiment": s_label, 
        "emotion": e_label
    }