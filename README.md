# 🛰️ Disruption Detector - AI-Powered News Analysis API

This project is an AI-based Flask API that fetches recent news from Indian cities using the **GNews API** and classifies whether the events are **disruptions** (like natural disasters, strikes, or protests) using a **zero-shot classification model** hosted on Hugging Face.

---

## 🔧 Features

- 🌐 Fetches recent English news from India related to:
  - Mumbai
  - Delhi
  - Bangalore
- 🧠 Uses Hugging Face's `facebook/bart-large-mnli` zero-shot model to classify news as:
  - Natural disaster
  - Weather disruption
  - Political protest
  - Transport strike
  - Power outage
  - Positive event
  - Not a disruption
- 🗂️ Returns only relevant disruption news in JSON format
- 🧪 Designed to be deployed as a REST API on Render

---

## 🛠️ Tech Stack

- Python 3.11+
- Flask
- Hugging Face Inference API
- GNews API
- dotenv for environment variables

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/disruption-detector.git
cd disruption-detector
