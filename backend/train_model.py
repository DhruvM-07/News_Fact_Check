import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load datasets
fake_df = pd.read_csv("/Users/nakshatramankikar/GeekVisha2.0/backend/Fake.csv")
true_df = pd.read_csv("/Users/nakshatramankikar/GeekVisha2.0/backend/True.csv")

# Label the data
fake_df["label"] = 0  # Fake News → 0
true_df["label"] = 1  # Real News → 1

# Combine both datasets
df = pd.concat([fake_df, true_df], ignore_index=True)

# Shuffle data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Select features and labels
X = df["text"]  # News content
y = df["label"]  # Labels

# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a text processing & ML pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_df=0.7)),  # Convert text to TF-IDF vectors
    ("model", LogisticRegression())  # Logistic Regression for classification
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate model
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Model Training Complete! Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Ensure the backend folder exists
os.makedirs("backend", exist_ok=True)

# Save model
joblib.dump(pipeline, "backend/fake_news_model.pkl")
print("🎉 Model saved as 'backend/fake_news_model.pkl'!")
