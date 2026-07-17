import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="Threat Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Threat Analytics")

DATA_PATH = Path("data/processed/processed_dataset.parquet")

# -----------------------------------------------------
# LOAD DATA
# -----------------------------------------------------

if not DATA_PATH.exists():

    st.error("Processed dataset not found.")
    st.stop()

df = pd.read_parquet(DATA_PATH)

# -----------------------------------------------------
# KPIs
# -----------------------------------------------------

st.subheader("Dataset Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total URLs", len(df))

c2.metric("Features", len(df.columns)-3)

c3.metric("Threat Classes", df["type"].nunique())

c4.metric("Dataset Size",
          f"{round(df.memory_usage().sum()/1024/1024,2)} MB")

st.divider()

# -----------------------------------------------------
# CLASS DISTRIBUTION
# -----------------------------------------------------

st.subheader("Threat Distribution")

col1, col2 = st.columns(2)

with col1:

    pie = px.pie(
        df,
        names="type",
        title="Threat Categories"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with col2:

    bar = px.bar(
        df["type"].value_counts().reset_index(),
        x="type",
        y="count",
        color="type",
        title="Class Counts"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.divider()

# -----------------------------------------------------
# FEATURE SELECTOR
# -----------------------------------------------------

numeric_columns = [

    c for c in df.columns

    if df[c].dtype != "object"

    and c != "label"

]

feature = st.selectbox(

    "Select Feature",

    numeric_columns

)

# -----------------------------------------------------
# HISTOGRAM
# -----------------------------------------------------

st.subheader("Feature Distribution")

hist = px.histogram(

    df,

    x=feature,

    color="type",

    marginal="box",

    nbins=50

)

st.plotly_chart(

    hist,

    use_container_width=True

)

st.divider()

# -----------------------------------------------------
# BOXPLOT
# -----------------------------------------------------

st.subheader("Feature Comparison")

box = px.box(

    df,

    x="type",

    y=feature,

    color="type"

)

st.plotly_chart(

    box,

    use_container_width=True

)

st.divider()

# -----------------------------------------------------
# CORRELATION
# -----------------------------------------------------

st.subheader("Correlation Matrix")

corr = df[numeric_columns].corr()

heatmap = px.imshow(

    corr,

    aspect="auto",

    color_continuous_scale="Viridis"

)

st.plotly_chart(

    heatmap,

    use_container_width=True

)

st.divider()

# -----------------------------------------------------
# PREVIEW
# -----------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(

    df.head(100),

    use_container_width=True

)