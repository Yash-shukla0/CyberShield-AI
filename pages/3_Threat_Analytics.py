import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="Threat Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Threat Analytics")

st.write(
    "Analytics and statistics of the CyberShield AI threat detection dataset."
)

# -----------------------------------------------------
# DATASET STATISTICS
# -----------------------------------------------------

TOTAL_URLS = 641119
TOTAL_FEATURES = 43
TOTAL_CLASSES = 4
DATASET_SIZE = "Processed dataset"

THREAT_COUNTS = {
    "Benign": 428080,
    "Defacement": 95308,
    "Malware": 23645,
    "Phishing": 94086
}

# -----------------------------------------------------
# DATAFRAME FOR CHARTS
# -----------------------------------------------------

threat_df = pd.DataFrame({
    "Class": list(THREAT_COUNTS.keys()),
    "Count": list(THREAT_COUNTS.values())
})

threat_df["Percentage"] = (
    threat_df["Count"] / TOTAL_URLS * 100
).round(2)

# -----------------------------------------------------
# DATASET STATISTICS
# -----------------------------------------------------

st.subheader("📊 Dataset Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total URLs",
    f"{TOTAL_URLS:,}"
)

col2.metric(
    "Features",
    TOTAL_FEATURES
)

col3.metric(
    "Threat Classes",
    TOTAL_CLASSES
)

col4.metric(
    "Dataset Size",
    DATASET_SIZE
)

st.divider()

# -----------------------------------------------------
# THREAT DISTRIBUTION
# -----------------------------------------------------

st.subheader("🚨 Threat Distribution")

c1, c2 = st.columns(2)

with c1:

    fig_pie = px.pie(
        threat_df,
        names="Class",
        values="Count",
        title="URL Classification Distribution"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

with c2:

    fig_bar = px.bar(
        threat_df,
        x="Class",
        y="Count",
        text="Count",
        title="Number of URLs by Class"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

st.divider()

# -----------------------------------------------------
# CLASS TABLE
# -----------------------------------------------------

st.subheader("📋 Threat Class Statistics")

display_df = threat_df.copy()

display_df["Count"] = display_df["Count"].map(
    lambda x: f"{x:,}"
)

display_df["Percentage"] = display_df[
    "Percentage"
].map(
    lambda x: f"{x:.2f}%"
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------------------------------
# FEATURE INFORMATION
# -----------------------------------------------------

st.subheader("🔍 Feature Information")

feature_names = [
    "URL Length",
    "Hostname Length",
    "Path Length",
    "Number of Dots",
    "Number of Hyphens",
    "Number of Digits",
    "Number of Special Characters",
    "Number of Subdomains",
    "HTTPS",
    "IP Address",
    "Shortened URL",
    "Suspicious TLD",
    "Query Length",
    "Fragment Length",
    "Entropy",
    "Digit Ratio",
    "Letter Ratio",
    "Special Character Ratio"
]

feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Category": [
        "Lexical",
        "Lexical",
        "Lexical",
        "Lexical",
        "Lexical",
        "Lexical",
        "Lexical",
        "Domain",
        "Security",
        "Domain",
        "Security",
        "Domain",
        "Lexical",
        "Lexical",
        "Statistical",
        "Statistical",
        "Statistical",
        "Statistical"
    ]
})

st.write(
    f"CyberShield AI uses **{TOTAL_FEATURES} engineered URL features** "
    "for threat classification."
)

st.dataframe(
    feature_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------------------------------
# FEATURE DISTRIBUTION
# -----------------------------------------------------

st.subheader("📐 Feature Distribution")

selected_feature = st.selectbox(
    "Select Feature",
    feature_df["Feature"].tolist()
)

st.info(
    f"**{selected_feature}** is one of the engineered URL features "
    "used by CyberShield AI during feature extraction."
)

st.divider()

# -----------------------------------------------------
# FEATURE COMPARISON
# -----------------------------------------------------

st.subheader("⚖️ Feature Comparison")

comparison_df = pd.DataFrame({
    "Class": [
        "Benign",
        "Defacement",
        "Malware",
        "Phishing"
    ],
    "URLs": [
        428080,
        95308,
        23645,
        94086
    ]
})

fig_comparison = px.bar(
    comparison_df,
    x="Class",
    y="URLs",
    color="Class",
    title="Class-wise Dataset Comparison"
)

st.plotly_chart(
    fig_comparison,
    use_container_width=True
)

st.divider()

# -----------------------------------------------------
# CORRELATION MATRIX
# -----------------------------------------------------

st.subheader("🔗 Correlation Matrix")

st.info(
    "The full processed feature matrix is not loaded in the deployed "
    "application. This avoids exposing the original dataset and keeps "
    "the deployment lightweight."
)

st.warning(
    "Correlation analysis is available during local model development "
    "where the complete processed dataset is available."
)

st.divider()

# -----------------------------------------------------
# SUMMARY
# -----------------------------------------------------

st.subheader("📌 Analytics Summary")

summary = pd.DataFrame({
    "Metric": [
        "Total Samples",
        "Engineered Features",
        "Classification Classes",
        "Largest Class",
        "Smallest Class"
    ],
    "Value": [
        f"{TOTAL_URLS:,}",
        TOTAL_FEATURES,
        TOTAL_CLASSES,
        "Benign",
        "Malware"
    ]
})

st.table(summary)

st.success(
    "🛡️ CyberShield AI threat analytics is operational."
)