from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import joblib
import os

Base = declarative_base()

# NewsArticle Model for Database Storage
class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    content = Column(String, nullable=False)
    credibility_score = Column(Float, nullable=False)
    credibility_status = Column(String, nullable=False)

# Load Pre-trained Fake News Detection Model
MODEL_PATH = "backend/fake_news_model.pkl"

if os.path.exists(MODEL_PATH):
    fake_news_model = joblib.load(MODEL_PATH)
else:
    fake_news_model = None
    print("⚠️ Fake News Model not found! Train and save the model first.")
