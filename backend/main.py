from fastapi import FastAPI
from pydantic import BaseModel
from credibility import analyze_credibility

app = FastAPI()

# Define request structure
class NewsData(BaseModel):
    text: str
    url: str

@app.post("/analyze")
async def analyze_news(data: NewsData):
    """
    Receives news content & URL from the Chrome extension,
    then analyzes credibility using the credibility module.
    """
    result = analyze_credibility(data.text, data.url)
    return result
