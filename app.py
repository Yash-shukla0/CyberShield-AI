import streamlit as st
from pathlib import Path
import pandas as pd


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.hero{
    background: linear-gradient(90deg,#0f172a,#111827);
    padding:35px;
    border-radius:18px;
    border:1px solid #374151;
}

.hero h1{
    color:white;
    font-size:42px;
}

.hero p{
    color:#d1d5db;
    font-size:18px;
}

.metric-card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #374151;
}

.feature-card{
    background:#1E293B;
    padding:22px;
    border-radius:16px;
    border:1px solid #475569;
    min-height:250px;
}

.feature-card h3{
    color:#38BDF8;
    font-size:32px;
    margin-bottom:20px;
}

.feature-card p{
    color:#F8FAFC;
    font-size:18px;
    line-height:1.8;
}


.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/shield.png",
        width=90
    )

    st.title("CyberShield AI")

    st.caption("AI-Based Cyber Threat Detection Framework")

    st.divider()

    st.success("🟢 System Status : Online")

    st.info("""
Current Prediction Engine

• XGBoost (Baseline)

Future Versions

• CNN

• BiLSTM

• Ensemble Learning

• Explainable AI
""")

    st.divider()

    st.subheader("Navigation")

    st.page_link("app.py", label="🏠 Home")

    st.page_link(
        "pages/1_Dashboard.py",
        label="📊 Dashboard"
    )

    st.page_link(
        "pages/2_URL_Detection.py",
        label="🔍 URL Detection"
    )

    st.page_link(
        "pages/3_Threat_Analytics.py",
        label="📈 Threat Analytics"
    )

    st.page_link(
        "pages/4_Model_Performance.py",
        label="🤖 Model Performance"
    )

    st.page_link(
        "pages/5_Prediction_History.py",
        label="📜 Prediction History"
    )

    st.page_link(
        "pages/6_About.py",
        label="ℹ️ About"
    )
    st.page_link(
        "pages/7_Explainable_AI.py",
        label="🧠 Explainable AI"
    )

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🛡️ CyberShield AI</h1>

<p>

Intelligent Cyber Threat Detection using Machine Learning
Analyze URLs, detect phishing attacks,
understand prediction reasoning,
and visualize cyber threats through
an interactive dashboard.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------------
# KPI SECTION
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

history_file = Path("history/prediction_history.csv")

if history_file.exists():
    history = pd.read_csv(history_file)
    total_predictions = len(history)
else:
    total_predictions = 0

with col1:
    st.metric(
        "Threats Detected",
        total_predictions
    )

with col2:
    st.metric(
        "Model Accuracy",
        "93.35%"
    )

with col3:
    st.metric(
        "Risk Engine",
        "Active"
    )

with col4:
    st.metric(
        "Prediction History",
        total_predictions
    )

st.divider()

# ---------------------------------------------------------
# FEATURES
# ---------------------------------------------------------

st.subheader("🚀 Core Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
<div class="feature-card">

<h3>🔍 URL Threat Detection</h3>

✔ Detect malicious URLs

✔ Phishing detection

✔ Confidence score

✔ Threat level

✔ Instant prediction

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="feature-card">

<h3>📊 Threat Analytics</h3>

✔ Interactive charts

✔ Dataset insights

✔ Feature importance

✔ Threat distribution

✔ Detection statistics

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="feature-card">

<h3>🧠 Explainable AI</h3>

✔ SHAP

✔ Feature contribution

✔ Transparent predictions

✔ AI reasoning

✔ Model interpretability

</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# WORKFLOW
# ---------------------------------------------------------

st.subheader("⚙️ Detection Workflow")

st.info("""
User URL

⬇

Feature Extraction

⬇

Machine Learning 

⬇

Threat Classification

⬇

Risk Score

⬇

Explainable AI

⬇

Final Report
""")

st.divider()

# ---------------------------------------------------------
# PROJECT ROADMAP
# ---------------------------------------------------------

st.subheader("🛣️ Project Roadmap")

st.progress(10)

tasks = [
    "✅ Project Structure",
    "🟡 Dataset Collection",
    "🟡 Exploratory Data Analysis",
    "🟡 Feature Engineering",
    "🟡 Machine Learning Models",
    "🟡 Explainable AI",
    "🟡 Streamlit Dashboard",
    "🟡 Deployment"
]

for task in tasks:
    st.write(task)

st.divider()

# ---------------------------------------------------------
# TECHNOLOGY STACK
# ---------------------------------------------------------

st.subheader("💻 Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.success("Python")

tech2.success("Streamlit")

tech3.success("Scikit-learn")

tech4.success("XGBoost")

tech5, tech6, tech7, tech8 = st.columns(4)

tech5.success("Pandas")

tech6.success("SHAP")

tech7.success("Plotly")

tech8.success("Pathlib")

st.divider()

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div class='footer'>

CyberShield AI © 2026

Developed by Yash Shukla

Powered by Python • Streamlit • Machine Learning • Deep Learning • Explainable AI

</div>
""", unsafe_allow_html=True)