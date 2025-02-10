from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define database file path
DATABASE_URL = "sqlite:///./news_credibility.db"

# Create engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define base model
Base = declarative_base()

# Define NewsArticle model
class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    credibility_score = Column(Integer, nullable=False)
    credibility_status = Column(String, nullable=False)

# Create tables if they don't exist
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database when script runs
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
