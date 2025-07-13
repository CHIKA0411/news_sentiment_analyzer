# scraper.py

from newspaper import Article
from newspaper import build

def scrape_ndtv():
    paper = build('https://www.ndtv.com/latest', memoize_articles=False)
    headlines = []

    for article in paper.articles[:10]:  # Limit to 10 for speed
        try:
            article.download()
            article.parse()
            headlines.append(article.title)
        except:
            continue

    return headlines

# Test
if __name__ == "__main__":
    print(scrape_ndtv())
