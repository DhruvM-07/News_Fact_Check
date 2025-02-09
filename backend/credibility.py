import requests
from bs4 import BeautifulSoup

# Use News API or NewsData.io (Choose One)
NEWS_API_KEY = "caf52e28652e4fcea5e4e3adea3d365b"  # Get from https://newsapi.org/
NEWSDATA_API_KEY = "pub_6859947508044f196cfb4b819934053e3929f"  # Get from https://newsdata.io/

def fetch_news_articles(query):
    """
    Fetch related news articles using News API or NewsData.io.
    """
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return articles
        else:
            print(f"Error fetching articles: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def scrape_news_website(url):
    """
    Scrape a news website to extract the article content.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            content = " ".join([p.get_text() for p in paragraphs])
            return content
        else:
            return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None
