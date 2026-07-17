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
# LOAD DATA
# -------------------------------------------------------

DATA_PATH = Path("data/processed/processed_dataset.parquet")

if DATA_PATH.exists():

    df = pd.read_parquet(DATA_PATH)

else:

    st.error("Processed dataset not found.")
    st.stop()

# -------------------------------------------------------
# KPI
# -------------------------------------------------------

total_urls = len(df)

benign = len(df[df["type"] == "benign"])

phishing = len(df[df["type"] == "phishing"])

malware = len(df[df["type"] == "malware"])

defacement = len(df[df["type"] == "defacement"])

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total URLs",
    f"{total_urls:,}"
)

col2.metric(
    "Benign",
    f"{benign:,}"
)

col3.metric(
    "Phishing",
    f"{phishing:,}"
)

col4.metric(
    "Malware",
    f"{malware:,}"
)

col5.metric(
    "Defacement",
    f"{defacement:,}"
)

st.divider()

# -------------------------------------------------------
# CLASS DISTRIBUTION
# -------------------------------------------------------

c1, c2 = st.columns(2)

with c1:

    fig = px.pie(
        df,
        names="type",
        title="Threat Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with c2:

    fig = px.bar(
        df["type"].value_counts(),
        title="Number of URLs per Class"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -------------------------------------------------------
# URL LENGTH
# -------------------------------------------------------

st.subheader("URL Length Distribution")

fig = px.histogram(
    df,
    x="url_length",
    nbins=50
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# TOP FEATURES
# -------------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# FEATURE SUMMARY
# -------------------------------------------------------

st.subheader("Feature Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# MODEL STATUS
# -------------------------------------------------------

st.subheader("Model Status")

status = pd.DataFrame({

    "Component":[

        "Dataset",
        "Feature Extraction",
        "Random Forest",
        "XGBoost",
        "Prediction API",
        "Dashboard"

    ],

    "Status":[

        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Ready",
        "✅ Running"

    ]

})

st.table(status)

st.success("CyberShield AI is operational.")