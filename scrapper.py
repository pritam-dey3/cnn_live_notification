import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
TARGET = "https://edition.cnn.com/europe/live-news/ukraine-russia-news-02-24-22-intl/"
PROXY = f"http://api.scraperapi.com?api_key={API_KEY}&url={TARGET}"


def get_headlines():
    while True:
        # try:
        print("sending request...")
        page = requests.get(PROXY)
        print("scraping...")
        soup = BeautifulSoup(page.content, "html.parser")
        headlines = soup.find_all("h2", class_="sc-dfVpRl kvaBeP")
        break
        # except Exception:
        #     continue
    headlines = [hl.text for hl in headlines]
    print("done.")
    return headlines[1:]
