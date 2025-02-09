import requests
from bs4 import BeautifulSoup

def scrape_news_website(url):
    """
    Scrapes the main content of a news article.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            content = " ".join([p.get_text() for p in paragraphs if p.get_text()])
            
            if content:
                return content
            else:
                return "Content not found."
        else:
            return "Failed to fetch the webpage."
    except Exception as e:
        print(f"Scraping error: {e}")
        return None
