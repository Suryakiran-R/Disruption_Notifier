import os
from flask import Flask, jsonify
from gnews_module import fetch_recent_articles
from classifier_module import classify_disruptions

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    return "✅ Disruption Classifier API is up!"

@app.route('/check_disruptions', methods=['POST'])
def check_disruptions():
    try:
        articles = fetch_recent_articles()
        if not articles:
            return jsonify({"message": "No recent articles found"}), 200

        disruption_results = classify_disruptions(articles)
        return jsonify(disruption_results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)