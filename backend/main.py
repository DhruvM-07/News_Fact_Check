from fastapi import FastAPI
from credibility import fetch_news_articles, scrape_news_website

app = FastAPI()

@app.get("/check-credibility/")
def check_credibility(news_title: str):
    """
    Fetches related news articles and checks credibility.
    """
    related_articles = fetch_news_articles(news_title)
    if not related_articles:
        return {"score": 35, "message": "No related news found. Credibility is unchecked."}

    # Example logic: if at least 3 related articles exist, assume it's more credible
    credibility_score = 50 + (len(related_articles) * 10)
    credibility_score = min(100, credibility_score)  # Cap at 100

    return {
        "score": credibility_score,
        "related_articles": [{"title": article["title"], "url": article["url"]} for article in related_articles],
    }
