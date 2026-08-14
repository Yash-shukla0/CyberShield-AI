import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CyberShield AI Dashboard")

st.write(
    "Overview of the dataset, model status and cyber threat distribution."
)

# -------------------------------------------------------
# DATASET SUMMARY
# -------------------------------------------------------

# Dataset statistics from the processed training dataset
DATASET_STATS = {
    "Benign": 428080,
    "Defacement": 95308,
    "Malware": 23645,
    "Phishing": 94086
}

total_urls = sum(DATASET_STATS.values())

# Create DataFrame for charts
distribution_df = pd.DataFrame({
    "Type": list(DATASET_STATS.keys()),
    "Count": list(DATASET_STATS.values())
})

# -------------------------------------------------------
# KPI
# -------------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total URLs",
    f"{total_urls:,}"
)

col2.metric(
    "Benign",
    f"{DATASET_STATS['Benign']:,}"
)

col3.metric(
    "Phishing",
    f"{DATASET_STATS['Phishing']:,}"
)

col4.metric(
    "Malware",
    f"{DATASET_STATS['Malware']:,}"
)

col5.metric(
    "Defacement",
    f"{DATASET_STATS['Defacement']:,}"
)

st.divider()

# -------------------------------------------------------
# CLASS DISTRIBUTION
# -------------------------------------------------------

c1, c2 = st.columns(2)

with c1:

    fig = px.pie(
        distribution_df,
        names="Type",
        values="Count",
        title="Threat Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with c2:

    fig = px.bar(
        distribution_df,
        x="Type",
        y="Count",
        text="Count",
        title="Number of URLs per Class"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -------------------------------------------------------
# DATASET INFORMATION
# -------------------------------------------------------

st.subheader("📁 Dataset Information")

info_col1, info_col2, info_col3 = st.columns(3)

info_col1.metric(
    "Total Samples",
    f"{total_urls:,}"
)

info_col2.metric(
    "Number of Features",
    "43"
)

info_col3.metric(
    "Classes",
    "4"
)

st.info(
    "Dataset statistics are displayed from the processed training dataset. "
    "The full dataset is not loaded into the deployed application."
)

st.divider()

# -------------------------------------------------------
# CLASS TABLE
# -------------------------------------------------------

st.subheader("📊 Class Distribution")

class_table = distribution_df.copy()

class_table["Percentage"] = (
    class_table["Count"] / total_urls * 100
).round(2)

class_table.columns = [
    "Class",
    "Samples",
    "Percentage"
]

st.dataframe(
    class_table,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -------------------------------------------------------
# MODEL PERFORMANCE
# -------------------------------------------------------

st.subheader("🤖 Model Performance")

performance_df = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        96.73,
        96.69,
        96.73,
        96.70
    ]
})

fig = px.bar(
    performance_df,
    x="Metric",
    y="Score",
    text="Score",
    title="Random Forest Model Performance"
)

fig.update_yaxes(
    range=[0, 100],
    title="Score (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# MODEL STATUS
# -------------------------------------------------------

st.subheader("⚙️ Model Status")

status = pd.DataFrame({

    "Component": [
        "Dataset",
        "Feature Extraction",
        "Random Forest",
        "XGBoost",
        "Prediction API",
        "Explainable AI",
        "Dashboard"
    ],

    "Status": [
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Running"
    ]
})

st.table(status)

st.success("🛡️ CyberShield AI is operational.")