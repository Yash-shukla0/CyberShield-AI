"""
CyberShield AI
Prediction Module
"""

from pathlib import Path

from datetime import datetime
import pandas as pd

import joblib

from src.feature_extractor import URLFeatureExtractor

from urllib.parse import urlparse

TRUSTED_DOMAINS = {
    "google.com",
    "www.google.com",
    "github.com",
    "www.github.com",
    "linkedin.com",
    "www.linkedin.com",
    "microsoft.com",
    "www.microsoft.com",
    "amazon.com",
    "www.amazon.com",
    "apple.com",
    "www.apple.com",
    "youtube.com",
    "www.youtube.com",
    "facebook.com",
    "www.facebook.com",
    "instagram.com",
    "www.instagram.com",
    "openai.com",
    "www.openai.com",
    "wikipedia.org",
    "www.wikipedia.org",
    "chatgpt.com",
    "www.chatgpt.com",
    "chat.openai.com",
    "docs.github.com",
    "mail.google.com",
    "drive.google.com",
    "accounts.google.com",
}

# -------------------------------------------------------
# PATHS
# -------------------------------------------------------

MODEL_DIR = Path("models")

MODEL = joblib.load(MODEL_DIR / "best_model.pkl")

FEATURE_COLUMNS = joblib.load(MODEL_DIR / "feature_columns.pkl")

LABEL_ENCODER = joblib.load("data/processed/label_encoder.pkl")


class URLPredictor:

    def __init__(self):
        self.model = MODEL

    def predict(self, url):

        extractor = URLFeatureExtractor(url)

        features = extractor.extract_dict()

        df = pd.DataFrame([features])

        df = df.reindex(columns=FEATURE_COLUMNS)

        prediction = self.model.predict(df)[0]

        probabilities = self.model.predict_proba(df)[0]

        label = LABEL_ENCODER.inverse_transform([prediction])[0]

        confidence = probabilities.max()

        return {

            "prediction": label,

            "confidence": round(confidence * 100, 2),

            "probabilities": {

                LABEL_ENCODER.inverse_transform([i])[0]: round(
                    probabilities[i] * 100, 2
                )

                for i in range(len(probabilities))

            }

        }


if __name__ == "__main__":

    predictor = URLPredictor()

    url = input("Enter URL: ")

    # -------------------------------------------------------
    # Extract Features
    # -------------------------------------------------------

    extractor = URLFeatureExtractor(url)

    features = extractor.extract_dict()

    print("\nExtracted Features:\n")

    for k, v in features.items():
        print(f"{k}: {v}")

    # -------------------------------------------------------
    # ML Prediction
    # -------------------------------------------------------

    result = predictor.predict(url)

    # -------------------------------------------------------
    # Trusted Domain Override
    # -------------------------------------------------------

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    trusted = {d.replace("www.", "") for d in TRUSTED_DOMAINS}

    is_trusted = any(
        domain == d or domain.endswith("." + d)
        for d in trusted
    )

    if is_trusted and result["prediction"] != "benign":

        result = {
            "prediction": "benign",
            "confidence": 99.99,
            "probabilities": {
                "benign": 99.99,
                "defacement": 0.0,
                "malware": 0.0,
                "phishing": 0.01,
            },
            "reason": "Official trusted domain detected. ML prediction overridden."
        }

    # -------------------------------------------------------
    # Save Prediction History
    # -------------------------------------------------------

    history_dir = Path("history")
    history_dir.mkdir(exist_ok=True)

    history_file = history_dir / "prediction_history.csv"

    row = pd.DataFrame([{
        "Timestamp": datetime.now(),
        "URL": url,
        "Prediction": result["prediction"],
        "Confidence": result["confidence"]
    }])

    if history_file.exists():
        old = pd.read_csv(history_file)
        row = pd.concat([old, row], ignore_index=True)

    row.to_csv(history_file, index=False)

    # -------------------------------------------------------
    # Print Result
    # -------------------------------------------------------

    print("\nPrediction:\n")
    print(result)

    if "reason" in result:
        print("\nReason:")
        print(result["reason"])

