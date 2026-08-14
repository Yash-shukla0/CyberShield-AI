"""
CyberShield AI
Prediction Module
"""

from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

import pandas as pd
import joblib

from src.feature_extractor import URLFeatureExtractor


# -------------------------------------------------------
# TRUSTED DOMAINS
# -------------------------------------------------------

TRUSTED_DOMAINS = {
    "google.com",
    "github.com",
    "linkedin.com",
    "microsoft.com",
    "amazon.com",
    "apple.com",
    "youtube.com",
    "facebook.com",
    "instagram.com",
    "openai.com",
    "wikipedia.org",
    "chatgpt.com",
    "netflix.com",
    "https://www.netflix.com/in/"

}


# -------------------------------------------------------
# PATHS
# -------------------------------------------------------

MODEL_DIR = Path("models")

MODEL = joblib.load(MODEL_DIR / "best_model.pkl")
FEATURE_COLUMNS = joblib.load(MODEL_DIR / "feature_columns.pkl")
LABEL_ENCODER = joblib.load(
    "data/processed/label_encoder.pkl"
)


# -------------------------------------------------------
# DOMAIN CHECK
# -------------------------------------------------------

def normalize_hostname(url):
    """
    Extract and normalize hostname from URL.
    """

    try:
        parsed = urlparse(url)

        hostname = parsed.hostname

        if not hostname:
            return None

        return hostname.lower().strip(".")

    except Exception:
        return None


def is_trusted_domain(url):
    """
    Check whether the URL belongs to a trusted registered domain.

    Examples:
        netflix.com              -> True
        www.netflix.com          -> True
        help.netflix.com         -> True
        netflix.com.attacker.com -> False
    """

    hostname = normalize_hostname(url)

    if not hostname:
        return False

    for domain in TRUSTED_DOMAINS:

        if hostname == domain:
            return True

        if hostname.endswith("." + domain):
            return True

    return False


# -------------------------------------------------------
# PREDICTOR
# -------------------------------------------------------

class URLPredictor:

    def __init__(self):
        self.model = MODEL

    def predict(self, url):

        # ------------------------------------------------
        # Extract Features
        # ------------------------------------------------

        extractor = URLFeatureExtractor(url)

        features = extractor.extract_dict()

        df = pd.DataFrame([features])

        df = df.reindex(columns=FEATURE_COLUMNS)

        # ------------------------------------------------
        # ML Prediction
        # ------------------------------------------------

        prediction = self.model.predict(df)[0]

        probabilities = self.model.predict_proba(df)[0]

        label = LABEL_ENCODER.inverse_transform(
            [prediction]
        )[0]

        confidence = probabilities.max()

        result = {
            "prediction": label,
            "confidence": round(confidence * 100, 2),
            "probabilities": {
                LABEL_ENCODER.inverse_transform([i])[0]:
                    round(probabilities[i] * 100, 2)
                for i in range(len(probabilities))
            }
        }

        # ------------------------------------------------
        # TRUSTED DOMAIN CHECK
        # ------------------------------------------------

        if is_trusted_domain(url):

            # Only override if ML predicts a malicious class
            if result["prediction"] != "benign":

                result["original_prediction"] = result["prediction"]
                result["original_confidence"] = result["confidence"]

                result["prediction"] = "benign"

                result["reason"] = (
                    "Recognized trusted registered domain. "
                    "ML prediction overridden."
                )

                # Do NOT fake 99.99% confidence.
                result["confidence"] = 99.0

                # Update probabilities consistently
                for key in result["probabilities"]:
                    result["probabilities"][key] = 0.0

                result["probabilities"]["benign"] = 99.0

        return result


# -------------------------------------------------------
# TEST
# -------------------------------------------------------

if __name__ == "__main__":

    predictor = URLPredictor()

    url = input("Enter URL: ")

    # ---------------------------------------------------
    # Extract Features
    # ---------------------------------------------------

    extractor = URLFeatureExtractor(url)

    features = extractor.extract_dict()

    print("\nExtracted Features:\n")

    for k, v in features.items():
        print(f"{k}: {v}")

    # ---------------------------------------------------
    # Prediction
    # ---------------------------------------------------

    result = predictor.predict(url)

    # ---------------------------------------------------
    # Save Prediction History
    # ---------------------------------------------------

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

        row = pd.concat(
            [old, row],
            ignore_index=True
        )

    row.to_csv(
        history_file,
        index=False
    )

    # ---------------------------------------------------
    # Print Result
    # ---------------------------------------------------

    print("\nPrediction:\n")
    print(result)

    if "reason" in result:

        print("\nReason:")
        print(result["reason"])

