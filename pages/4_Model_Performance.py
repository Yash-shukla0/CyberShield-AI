import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Model Performance")

st.write(
    "Performance evaluation of the machine learning models used "
    "in CyberShield AI."
)

# -------------------------------------------------------
# MODEL PERFORMANCE
# -------------------------------------------------------

accuracy = 96.73
precision = 96.69
recall = 96.73
f1_score = 96.70

# -------------------------------------------------------
# KPI CARDS
# -------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{accuracy:.2f}%"
)

col2.metric(
    "Precision",
    f"{precision:.2f}%"
)

col3.metric(
    "Recall",
    f"{recall:.2f}%"
)

col4.metric(
    "F1 Score",
    f"{f1_score:.2f}%"
)

st.divider()

# -------------------------------------------------------
# PERFORMANCE CHART
# -------------------------------------------------------

st.subheader("📊 Model Performance Metrics")

performance_df = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        accuracy,
        precision,
        recall,
        f1_score
    ]
})

fig = px.bar(
    performance_df,
    x="Metric",
    y="Score",
    text="Score",
    title="Random Forest Performance"
)

fig.update_yaxes(
    range=[0, 100],
    title="Score (%)"
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# MODEL INFORMATION
# -------------------------------------------------------

st.subheader("🧠 Model Information")

model_info = pd.DataFrame({
    "Component": [
        "Primary Model",
        "Classification Type",
        "Number of Classes",
        "Number of Features",
        "Training Samples",
        "Testing Samples"
    ],
    "Value": [
        "Random Forest",
        "Multi-Class Classification",
        "4",
        "43",
        "512,895",
        "128,224"
    ]
})

st.table(model_info)

st.divider()

# -------------------------------------------------------
# CLASS INFORMATION
# -------------------------------------------------------

st.subheader("🏷️ Supported URL Classes")

class_df = pd.DataFrame({
    "Class": [
        "Benign",
        "Defacement",
        "Malware",
        "Phishing"
    ],
    "Description": [
        "Legitimate and safe URLs",
        "URLs containing defaced or modified web content",
        "URLs associated with malicious software",
        "URLs designed to deceive users or steal information"
    ]
})

st.dataframe(
    class_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -------------------------------------------------------
# MODEL STATUS
# -------------------------------------------------------

st.subheader("⚙️ Model Status")

status = pd.DataFrame({
    "Component": [
        "Random Forest Model",
        "Feature Extractor",
        "Prediction Engine",
        "Explainable AI",
        "Streamlit Dashboard"
    ],
    "Status": [
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Running"
    ]
})

st.table(status)

st.success(
    "🛡️ CyberShield AI model is ready for URL threat classification."
)