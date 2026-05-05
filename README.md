# Bangla Sentiment Pro 🇧🇩
**A Dual-Head Deep Learning System for Sentiment & Emotion Classification**

## 📥 How to Get the Project 
# Open your terminal and run these commands to clone the repository:

git clone https://github.com/afrin2326/Bangla_Sentiment_Pro.git
cd Bangla_Sentiment_Pro


---

## 🛠 Prerequisites
* Python 3.8 or higher
* pip (Python Package Manager)

---

## 🚀 Setup & Installation

### Step 1: Create and Activate Virtual Environment
# Open your terminal and run the following commands:

# 1. Navigate to the project folder
cd Bangla_Sentiment_Pro

# 2. Create a virtual environment named 'venv'
python -m venv venv

# 3. Activate the environment (For Windows)
.\venv\Scripts\activate

# 3. Activate the environment (For macOS/Linux)
# source venv/bin/activate

---

### Step 2: Install Dependencies
# Install all required libraries using the requirements.txt file:

pip install -r requirements.txt

---

## 💻 How to Run the Project (রান করার নিয়ম)

### Step A: Start the Backend (FastAPI Server)
# Open a NEW terminal, activate the venv, and run the API:

uvicorn api.main:app --reload

# The API will be live at: http://127.0.0.1:8000

---

### Step B: Start the Frontend (Streamlit Dashboard)
# Open ANOTHER new terminal tab, activate the venv, and run the UI:

streamlit run webapp/app.py

# The dashboard will open automatically at: http://localhost:8501

---

## 📁 Project Structure
* **api/**: FastAPI backend logic and endpoints.
* **models/**: Pre-trained weights (.pt) and encoders (.pkl).
* **src/**: Model architecture and text preprocessing code.
* **webapp/**: Streamlit frontend interface.

---

