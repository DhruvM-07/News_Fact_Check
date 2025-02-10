import requests
import random

# API keys
NEWSAPI_KEY = "caf52e28652e4fcea5e4e3adea3d365b"
NEWSDATA_KEY = "pub_6859947508044f196cfb4b819934053e3929f"

def fact_check_news(text):
    """
    Check if the news exists in trusted sources using NewsAPI & NewsData.io.
    Returns a credibility score.
    """

    credibility_score = 50  # Default midpoint score

    # 🔹 1. Search in NewsAPI
    newsapi_url = f"https://newsapi.org/v2/everything?q={text[:10]}&apiKey={NEWSAPI_KEY}"
    response = requests.get(newsapi_url)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        if articles:
            credibility_score += 20  # Increase score if found in trusted sources

    # 🔹 2. Search in NewsData.io
    newsdata_url = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_KEY}&q={text[:10]}"
    response = requests.get(newsdata_url)

    if response.status_code == 200:
        articles = response.json().get("results", [])
        if articles:
            credibility_score += 20  # Increase score if found in NewsData.io

    return credibility_score


def analyze_credibility(text: str, url: str):
    """
    Analyze the credibility of news based on:
    1. Fact-checking with NewsAPI & NewsData.io
    2. Sentiment Analysis (Simplified for now)
    """

    # 🔹 Step 1: Fact-checking score
    credibility_score = fact_check_news(text)

    # 🔹 Step 2: Sentiment analysis (Placeholder, improve later)
    if "fake" in text.lower() or "hoax" in text.lower():
        credibility_score -= 15  # Reduce score for negative words
    elif "confirmed" in text.lower() or "official" in text.lower():
        credibility_score += 10  # Increase score for positive words

    # 🔹 Step 3: Assign a credibility classification
    classification = "Real" if credibility_score > 70 else "Fake" if credibility_score < 35 else "Unverified"

    return {
        "score": credibility_score,
        "classification": classification
    }
