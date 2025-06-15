import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = "http://books.toscrape.com/catalogue/page-1.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip().replace("£", "")
        availability = book.select_one(".availability").text.strip()
        books.append({
            "title": title,
            "price": float(price),
            "availability": availability
        })
    return books
