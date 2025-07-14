import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

CANDIDATE_LABELS = [
    "weather disruption", "transport strike", "political protest", "power outage",
    "natural disaster", "positive event", "not a disruption"
]

def classify_disruptions(articles):
    classified_articles = []

    for article in articles:
        text = f"{article['title']} {article.get('description', '')}".strip()
        if len(text) < 30:
            continue

        payload = {
            "inputs": text,
            "parameters": {
                "candidate_labels": CANDIDATE_LABELS,
                "multi_class": False
            }
        }

        try:
            response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, json=payload)
            result = response.json()

            if response.status_code == 200 and "labels" in result:
                top_label = result["labels"][0]
                score = result["scores"][0]

                if (top_label not in ["not a disruption", "positive event"]) and score >= 0.9:
                    article["predicted_label"] = top_label
                    article["confidence"] = round(score, 3)
                    classified_articles.append(article)

            time.sleep(1)

        except Exception as e:
            print(f"Error: {e}")

    return classified_articles
