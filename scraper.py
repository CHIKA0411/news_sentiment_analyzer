import requests
from bs4 import BeautifulSoup

def scrape_ndtv():
    url = "https://www.ndtv.com/latest"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []

    for item in soup.select("div.new_storylising h2 a"):
        title = item.get_text(strip=True)
        if title:
            headlines.append(title)

    return headlines
