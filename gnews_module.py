import requests
import time
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
GNEWS_URL = 'https://gnews.io/api/v4/search'

search_terms = [
    # Mumbai
    "flood Mumbai", "rain Mumbai", "heavy rain Mumbai", "traffic jam Mumbai",
    "heatwave Mumbai", "power outage Mumbai", "strike Mumbai", "protest Mumbai",
    "storm Mumbai", "earthquake Mumbai",

    # Bangalore
    "flood Bangalore", "rain Bangalore", "heavy rain Bangalore", "traffic jam Bangalore",
    "heatwave Bangalore", "power outage Bangalore", "strike Bangalore", "protest Bangalore",
    "storm Bangalore", "earthquake Bangalore",

    # Delhi
    "flood Delhi", "rain Delhi", "heavy rain Delhi", "traffic jam Delhi",
    "heatwave Delhi", "power outage Delhi", "strike Delhi", "protest Delhi",
    "storm Delhi", "earthquake Delhi",
]

def fetch_articles(query):
    params = {
        'q': query,
        'token': GNEWS_API_KEY,
        'lang': 'en',
        'country': 'in',
        'max': 10,
    }
    response = requests.get(GNEWS_URL, params=params)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        return []

def is_recent(article_date_str):
    try:
        published_time = datetime.fromisoformat(article_date_str.replace("Z", "+00:00"))
        return published_time > datetime.now(timezone.utc) - timedelta(days=7)
    except Exception:
        return False

def fetch_recent_articles():
    saved_articles = []
    for term in search_terms:
        articles = fetch_articles(term)
        for article in articles:
            if is_recent(article['publishedAt']):
                city = next((c for c in ["Mumbai", "Bangalore", "Delhi"] if c.lower() in term.lower()), "")
                saved_articles.append({
                    'keyword': term,
                    'location': city,
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url'],
                    'publishedAt': article['publishedAt']
                })
        time.sleep(1.2)
    return saved_articles
