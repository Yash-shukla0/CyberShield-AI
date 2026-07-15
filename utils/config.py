"""
=========================================================
CyberShield AI
Configuration File

Author : Yash Shukla
=========================================================
"""

from pathlib import Path

# -------------------------------------------------------
# Project Information
# -------------------------------------------------------

PROJECT_NAME = "CyberShield AI"

TAGLINE = "Intelligent Cyber Threat Detection with Explainable AI"

VERSION = "1.0.0"

AUTHOR = "Yash Shukla"

DESCRIPTION = (
    "CyberShield AI is an intelligent cybersecurity platform "
    "that detects malicious URLs using Machine Learning, "
    "Deep Learning, and Explainable AI."
)

# -------------------------------------------------------
# Project Root
# -------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------
# Folder Paths
# -------------------------------------------------------

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = ROOT_DIR / "models"

ASSET_DIR = ROOT_DIR / "assets"

HISTORY_DIR = ROOT_DIR / "history"

PAGES_DIR = ROOT_DIR / "pages"

SRC_DIR = ROOT_DIR / "src"

UTILS_DIR = ROOT_DIR / "utils"

# -------------------------------------------------------
# Dataset
# -------------------------------------------------------

DATASET_NAME = "Phishing URL Dataset"

DATASET_FILE = RAW_DATA_DIR / "phishing_urls.csv"

# -------------------------------------------------------
# Model Paths
# -------------------------------------------------------

RANDOM_FOREST_MODEL = MODEL_DIR / "random_forest.pkl"

XGBOOST_MODEL = MODEL_DIR / "xgboost.pkl"

CNN_MODEL = MODEL_DIR / "cnn_model.keras"

BILSTM_MODEL = MODEL_DIR / "bilstm_model.keras"

ENSEMBLE_MODEL = MODEL_DIR / "ensemble.pkl"

TOKENIZER_PATH = MODEL_DIR / "tokenizer.pkl"

SCALER_PATH = MODEL_DIR / "scaler.pkl"

LABEL_ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

# -------------------------------------------------------
# Prediction History
# -------------------------------------------------------

PREDICTION_HISTORY = HISTORY_DIR / "predictions.csv"

# -------------------------------------------------------
# Prediction Classes
# -------------------------------------------------------

CLASS_NAMES = [
    "Safe",
    "Malicious"
]

# -------------------------------------------------------
# Threat Levels
# -------------------------------------------------------

LOW_RISK = "LOW"

MEDIUM_RISK = "MEDIUM"

HIGH_RISK = "HIGH"

# -------------------------------------------------------
# Supported Models
# -------------------------------------------------------

SUPPORTED_MODELS = {
    "Random Forest": RANDOM_FOREST_MODEL,
    "XGBoost": XGBOOST_MODEL,
    "CNN": CNN_MODEL,
    "BiLSTM": BILSTM_MODEL,
    "Ensemble": ENSEMBLE_MODEL
}

# Default model
ACTIVE_MODEL = "XGBoost"

# -------------------------------------------------------
# UI Settings
# -------------------------------------------------------

PRIMARY_COLOR = "#00BFFF"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#EAB308"

DANGER_COLOR = "#DC2626"

BACKGROUND_COLOR = "#0F172A"

CARD_COLOR = "#1E293B"

TEXT_COLOR = "#FFFFFF"

# -------------------------------------------------------
# Streamlit
# -------------------------------------------------------

PAGE_TITLE = PROJECT_NAME

PAGE_ICON = "🛡️"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

# -------------------------------------------------------
# Feature Engineering
# -------------------------------------------------------

MAX_URL_LENGTH = 2048

MAX_DOMAIN_LENGTH = 253

MAX_SUBDOMAIN_LENGTH = 63

# -------------------------------------------------------
# Training Parameters
# -------------------------------------------------------

TEST_SIZE = 0.20

RANDOM_STATE = 42

CV_FOLDS = 5

# -------------------------------------------------------
# Deep Learning Parameters
# -------------------------------------------------------

SEQUENCE_LENGTH = 200

VOCAB_SIZE = 5000

EMBEDDING_DIM = 128

LSTM_UNITS = 128

BATCH_SIZE = 32

EPOCHS = 20

# -------------------------------------------------------
# Confidence Thresholds
# -------------------------------------------------------

HIGH_CONFIDENCE = 0.90

MEDIUM_CONFIDENCE = 0.70

LOW_CONFIDENCE = 0.50

# -------------------------------------------------------
# Application Information
# -------------------------------------------------------

COPYRIGHT = "© 2026 CyberShield AI"

LICENSE = "MIT License"

GITHUB_REPO = "https://github.com/YOUR_USERNAME/CyberShield-AI"
