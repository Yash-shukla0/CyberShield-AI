import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
import plotly.express as px
from src.explain import URLExplainer

from src.predict import URLPredictor
from src.feature_extractor import URLFeatureExtractor

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------

st.set_page_config(
    page_title="URL Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ URL Threat Detection")

st.write(
    "Enter a URL below and let CyberShield AI classify it."
)

predictor = URLPredictor()

# --------------------------------------------------------
# INPUT
# --------------------------------------------------------

url = st.text_input(
    "Enter URL",
    placeholder="https://google.com"
)

# --------------------------------------------------------
# BUTTON
# --------------------------------------------------------

if st.button("Analyze URL", use_container_width=True):

    if url.strip() == "":
        st.warning("Please enter a URL.")
        st.stop()

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    result = predictor.predict(url)

    predicted_label = result["prediction"].capitalize()
    confidence = result["confidence"]

    # --------------------------------------------------------
    # Trusted Domain Override
    # --------------------------------------------------------

    from urllib.parse import urlparse
    from src.predict import TRUSTED_DOMAINS

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    trusted = {d.replace("www.", "") for d in TRUSTED_DOMAINS}

    is_trusted = any(
        domain == d or domain.endswith("." + d)
        for d in trusted
    )

    if is_trusted:

        predicted_label = "Benign"

        confidence = 99.99

        result["prediction"] = "benign"
        result["confidence"] = 99.99

        result["probabilities"] = {
            "benign": 99.99,
            "defacement": 0.0,
            "malware": 0.0,
            "phishing": 0.01
        }
    
    # -------------------------------
    # Save Prediction History
    # -------------------------------

    history_dir = Path("history")
    history_dir.mkdir(exist_ok=True)

    history_file = history_dir / "prediction_history.csv"

    row = pd.DataFrame([{
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "URL": url,
        "Prediction": result["prediction"],
        "Confidence": result["confidence"]
    }])

    if history_file.exists():
        old = pd.read_csv(history_file)
        row = pd.concat([old, row], ignore_index=True)

    row.to_csv(history_file, index=False)

    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    st.divider()

    if predicted_label.lower() == "benign":
        st.success(f"### ✅ Prediction : {predicted_label}")

    elif predicted_label.lower() == "phishing":
        st.error(f"### 🚨 Prediction : {predicted_label}")

    elif predicted_label.lower() == "malware":
        st.error(f"### ☠️ Prediction : {predicted_label}")

    else:
        st.warning(f"### ⚠️ Prediction : {predicted_label}")

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    # --------------------------------------------------------
    # Probability Chart
    # --------------------------------------------------------

    st.subheader("Prediction Probability")

    prob_df = pd.DataFrame({
        "Class": list(result["probabilities"].keys()),
        "Probability": list(result["probabilities"].values())
    })

    fig = px.bar(
        prob_df,
        x="Class",
        y="Probability",
        text="Probability",
        color="Probability",
        title="Prediction Probability"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # Extracted Features
    # --------------------------------------------------------

    st.subheader("Extracted Features")

    extractor = URLFeatureExtractor(url)

    features = extractor.extract_dict()

    explainer = URLExplainer()

    explanation = explainer.explain(features)

    feature_df = pd.DataFrame(
        features.items(),
        columns=["Feature", "Value"]
    )

    st.dataframe(
        feature_df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------------
    # Risk Meter
    # --------------------------------------------------------

    st.subheader("Risk Score")

    st.progress(int(confidence))

    if confidence >= 90:
        st.success("Very High Confidence")

    elif confidence >= 70:
        st.info("High Confidence")

    elif confidence >= 50:
        st.warning("Moderate Confidence")

    else:
        st.error("Low Confidence")

    st.divider()

    st.subheader("🧠 Explainable AI")

    st.info(
        "Top features that influenced this prediction."
    )

    st.dataframe(
        explanation,
        use_container_width=True,
        hide_index=True
    )