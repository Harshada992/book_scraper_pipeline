import requests
from bs4 import BeautifulSoup
import pandas as pd

def smart_scrape(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch URL: {url} (Status code: {response.status_code})")

    content_type = response.headers.get("Content-Type", "")
    if "text/html" not in content_type:
        raise Exception("URL does not point to an HTML page.")

    try:
        # Try to parse tables first
        tables = pd.read_html(response.text)
        if tables:
            return tables[0].to_dict(orient="records")
    except ValueError:
        pass  # No tables found

    # Fallback to basic text/card scraping
    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for tag in soup.find_all(["h1", "h2", "p", "li"], limit=50):
        if tag.get_text(strip=True):
            data.append({"content": tag.get_text(strip=True)})
    return data
