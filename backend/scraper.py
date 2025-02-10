import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fetch_article_content(url):
    """
    Fetches and extracts the main article content from a given news URL.
    
    Args:
        url (str): The news article URL.
    
    Returns:
        str: Extracted article text or an error message.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP issues

        soup = BeautifulSoup(response.text, "html.parser")

        # Try extracting article content from common tags
        article_text = ""
        for tag in ["article", "div", "section"]:
            content = soup.find(tag)
            if content:
                article_text = " ".join(p.get_text() for p in content.find_all("p"))
                if len(article_text) > 200:  # Ensure meaningful content
                    break

        if not article_text:
            return "Error: Could not extract article content."

        return article_text.strip()

    except requests.exceptions.RequestException as e:
        return f"Error: Failed to fetch content. {str(e)}"

if __name__ == "__main__":
    test_url = "https://www.bbc.com/news/world-us-canada-60181071"
    print(fetch_article_content(test_url))
