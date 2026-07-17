import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Explainable AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explainable AI")

st.write(
    "Understand how CyberShield AI makes predictions."
)

# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

st.header("📊 Feature Importance")

image_path = Path("reports/feature_importance.png")

if image_path.exists():
    st.image(str(image_path), use_container_width=True)
else:
    st.warning("feature_importance.png not found. Train the model first.")

# --------------------------------------------------
# PREDICTION HISTORY ANALYSIS
# --------------------------------------------------

st.header("📈 Prediction History Analysis")

history_path = Path("history/prediction_history.csv")

if history_path.exists():

    history = pd.read_csv(history_path)

    st.dataframe(history, use_container_width=True)

    if len(history) > 0:

        fig = px.histogram(
            history,
            x="Prediction",
            color="Prediction",
            title="Prediction Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info("No prediction history available.")

# --------------------------------------------------
# ABOUT EXPLAINABLE AI
# --------------------------------------------------

st.header("🧠 What is Explainable AI?")

st.success("""
Explainable AI (XAI) helps users understand why the machine learning model
classified a URL as Benign, Phishing, Malware, or Defacement.

CyberShield AI analyzes dozens of URL features such as:

• URL Length

• HTTPS Usage

• IP Address Presence

• Number of Dots

• Entropy

• Suspicious Keywords

• Domain Length

• Special Characters

These features collectively determine the final prediction.
""")