import requests
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import html2text

def search_duckduckgo(query: str, max_results: int = 5):
    """Searches DuckDuckGo and returns a list of results."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            return results
    except Exception as e:
        print(f"Error searching DuckDuckGo: {e}")
        return []

def fetch_page_content(url: str, timeout: int = 10):
    """Fetches and parses the content of a web page."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
            
        text = soup.get_text()
        
        # Convert to cleaner text
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        return h.handle(response.text)[:5000] # Limit content length
        
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return "Could not fetch content."
