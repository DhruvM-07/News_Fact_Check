import pickle
import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class FakeNewsModel:
    def __init__(self):
        # Load the trained model & vectorizer
        model_path = os.path.join(os.path.dirname(__file__), "fake_news_model.pkl")
        vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

        self.vectorizer = joblib.load(vectorizer_path)
        self.model = joblib.load(model_path)

    def predict(self, text):
        """Predicts if the news is Fake or Real"""
        text_transformed = self.vectorizer.transform([text])
        prediction = self.model.predict(text_transformed)
        return "Real" if prediction[0] == 1 else "Fake"
