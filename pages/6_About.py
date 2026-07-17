import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ",
    layout="wide"
)

st.title("ℹ About CyberShield AI")

st.markdown("---")

st.header("🛡 Project")

st.write("""

CyberShield AI is an AI-powered cyber threat detection framework developed by - Yash Shukla
designed to identify malicious URLs using Machine Learning.

The system extracts lexical, domain and statistical features
from URLs and predicts whether a URL is:

• Benign

• Phishing

• Malware

• Defacement

""")

st.markdown("---")

st.header("⚙ Technologies")

st.write("""

• Python

• Streamlit

• Pandas

• Scikit-Learn

• XGBoost

• Plotly

• Joblib

• SHAP 

• TensorFlow (Upcoming)

""")

st.markdown("---")

st.header("📂 Features")

st.write("""

✔ URL Feature Extraction

✔ Threat Classification

✔ Confidence Score

✔ Prediction History

✔ Analytics Dashboard

✔ Model Performance

✔ Interactive Visualizations

✔ Explainable AI 

""")

st.markdown("---")

st.header("📊 Dataset")

st.write("""

Dataset contains four classes:

• Benign

• Phishing

• Malware

• Defacement

More than 6 lakh URLs were used for training.

""")

st.markdown("---")

st.header("👨‍💻 Developer")

st.success("Yash Shukla")

st.write("""

B.Tech (Artificial Intelligence & Machine Learning)

Cyber Security & Machine Learning Enthusiast

Project:
CyberShield AI – AI-Based Cyber Threat Detection Framework

""")

st.markdown("---")

st.caption("CyberShield AI © 2026")