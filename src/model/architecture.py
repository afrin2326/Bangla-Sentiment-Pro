import torch.nn as nn
from transformers import AutoModel

class BanglaSentimentEmotionModel(nn.Module):
    def __init__(self, num_sentiments=5, num_emotions=7, dropout=0.1):
        super().__init__()
        # Updated to the correct base model that matches your 32,000 vocab size weights
        self.banglabert = AutoModel.from_pretrained("csebuetnlp/banglabert")
        
        hidden_size = self.banglabert.config.hidden_size
        self.dropout = nn.Dropout(dropout)
        self.sentiment_head = nn.Linear(hidden_size, num_sentiments)
        self.emotion_head = nn.Linear(hidden_size, num_emotions)

    def forward(self, input_ids, attention_mask):
        outputs = self.banglabert(input_ids=input_ids, attention_mask=attention_mask)
        # Using the [CLS] token (first token) for classification
        pooled = outputs.last_hidden_state[:, 0, :]
        pooled = self.dropout(pooled)
        
        sentiment_logits = self.sentiment_head(pooled)
        emotion_logits = self.emotion_head(pooled)
        
        return sentiment_logits, emotion_logits