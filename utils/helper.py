"""
=========================================================
CyberShield AI

Utility Functions

Author : Yash Shukla
=========================================================
"""

from datetime import datetime
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st
import validators
import tldextract

from utils.config import (
    RANDOM_FOREST_MODEL,
    XGBOOST_MODEL,
    CNN_MODEL,
    BILSTM_MODEL,
    ENSEMBLE_MODEL,
    ACTIVE_MODEL,
    HIGH_CONFIDENCE,
    MEDIUM_CONFIDENCE,
    PREDICTION_HISTORY
)


# -------------------------------------------------------
# URL VALIDATION
# -------------------------------------------------------

def is_valid_url(url: str) -> bool:
    """
    Returns True if URL is valid.
    """
    return validators.url(url)


# -------------------------------------------------------
# DOMAIN EXTRACTION
# -------------------------------------------------------

def extract_domain(url: str) -> dict:
    """
    Extract domain information.
    """

    result = tldextract.extract(url)

    return {
        "subdomain": result.subdomain,
        "domain": result.domain,
        "suffix": result.suffix
    }


# -------------------------------------------------------
# CONFIDENCE
# -------------------------------------------------------

def confidence_percentage(probability):

    return round(probability * 100, 2)


# -------------------------------------------------------
# THREAT LEVEL
# -------------------------------------------------------

def threat_level(probability):

    if probability >= HIGH_CONFIDENCE:
        return "🔴 HIGH"

    elif probability >= MEDIUM_CONFIDENCE:
        return "🟠 MEDIUM"

    else:
        return "🟢 LOW"


# -------------------------------------------------------
# CURRENT TIME
# -------------------------------------------------------

def current_time():

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# -------------------------------------------------------
# SAVE HISTORY
# -------------------------------------------------------

def save_prediction(
    url,
    prediction,
    confidence,
    risk
):

    Path(PREDICTION_HISTORY).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    row = pd.DataFrame({

        "Timestamp":[current_time()],
        "URL":[url],
        "Prediction":[prediction],
        "Confidence":[confidence],
        "Risk":[risk]

    })

    if Path(PREDICTION_HISTORY).exists():

        old = pd.read_csv(PREDICTION_HISTORY)

        row = pd.concat(
            [old, row],
            ignore_index=True
        )

    row.to_csv(
        PREDICTION_HISTORY,
        index=False
    )


# -------------------------------------------------------
# LOAD HISTORY
# -------------------------------------------------------

def load_history():

    if Path(PREDICTION_HISTORY).exists():

        return pd.read_csv(PREDICTION_HISTORY)

    return pd.DataFrame(
        columns=[
            "Timestamp",
            "URL",
            "Prediction",
            "Confidence",
            "Risk"
        ]
    )


# -------------------------------------------------------
# CLEAR HISTORY
# -------------------------------------------------------

def clear_history():

    if Path(PREDICTION_HISTORY).exists():

        Path(PREDICTION_HISTORY).unlink()


# -------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------

@st.cache_resource
def load_model():

    models = {

        "Random Forest": RANDOM_FOREST_MODEL,

        "XGBoost": XGBOOST_MODEL,

        "CNN": CNN_MODEL,

        "BiLSTM": BILSTM_MODEL,

        "Ensemble": ENSEMBLE_MODEL
    }

    model_path = models.get(ACTIVE_MODEL)

    if Path(model_path).exists():

        return joblib.load(model_path)

    return None


# -------------------------------------------------------
# BADGE
# -------------------------------------------------------

def prediction_badge(prediction):

    if prediction == "Safe":

        return "🟢 Safe"

    return "🔴 Malicious"


# -------------------------------------------------------
# PAGE HEADER
# -------------------------------------------------------

def page_header(title, subtitle):

    st.title(title)

    st.caption(subtitle)

    st.divider()


# -------------------------------------------------------
# EMPTY CHART DATA
# -------------------------------------------------------

def empty_chart():

    return pd.DataFrame({

        "Threat": [],

        "Count": []

    })


# -------------------------------------------------------
# MODEL STATUS
# -------------------------------------------------------

def model_status():

    model = load_model()

    if model is None:

        return "❌ Model Not Available"

    return "✅ Model Loaded"


# -------------------------------------------------------
# SYSTEM INFO
# -------------------------------------------------------

def system_information():

    return {

        "Active Model": ACTIVE_MODEL,

        "Python": "3.11+",

        "Framework": "Streamlit",

        "Prediction Engine": "Machine Learning / Deep Learning"

    }