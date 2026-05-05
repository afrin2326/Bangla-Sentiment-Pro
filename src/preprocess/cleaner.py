import re
from bnunicodenormalizer import Normalizer

class BanglaPreProcessor:
    def __init__(self):
        # Initialize the Bangla Unicode Normalizer
        self.norm = Normalizer()

    def clean_text(self, text):
        """
        Cleans and normalizes Bangla text by removing URLs, 
        mentions, and applying unicode normalization.
        """
        if not text:
            return ""

        # 1. Remove URLs (http, https, www)
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

        # 2. Remove User Mentions and Hashtags (Optional but recommended)
        text = re.sub(r'@\S+|#\S+', '', text)

        # 3. Unicode Normalization
        # This ensures that characters like 'ড়' are treated consistently 
        # (Normalization form: NFC)
        words = text.split()
        normalized_words = []
        
        for word in words:
            normalized = self.norm.normalize(word)
            # 'result' contains the normalized string
            normalized_words.append(normalized['result'])
            
        return " ".join(normalized_words)

# Example usage (for testing):
# prep = BanglaPreProcessor()
# print(prep.clean_text("আমি ভালো আছি! http://example.com"))