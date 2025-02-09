from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./news.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class NewsRecord(Base):
    """Database model for storing news records."""
    __tablename__ = "news"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    credibility_score = Column(Integer, nullable=False)

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)

init_db()
