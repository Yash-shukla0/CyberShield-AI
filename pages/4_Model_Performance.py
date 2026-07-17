import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Model Performance")

# ----------------------------------------------------
# PATHS
# ----------------------------------------------------

DATA_PATH = Path("data/processed/processed_dataset.parquet")
MODEL_PATH = Path("models/best_model.pkl")

if not DATA_PATH.exists():

    st.error("Processed dataset not found.")

    st.stop()

if not MODEL_PATH.exists():

    st.error("Train the model first.")

    st.stop()

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = pd.read_parquet(DATA_PATH)

df = df.dropna()

X = df.drop(columns=["url","type","label"])

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# ----------------------------------------------------
# LOAD MODEL
# ----------------------------------------------------

model = joblib.load(MODEL_PATH)

# ----------------------------------------------------
# PREDICTION
# ----------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted"
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

# ----------------------------------------------------
# METRICS
# ----------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("Accuracy",f"{accuracy*100:.2f}%")
c2.metric("Precision",f"{precision:.4f}")
c3.metric("Recall",f"{recall:.4f}")
c4.metric("F1 Score",f"{f1:.4f}")

st.divider()

# ----------------------------------------------------
# CLASSIFICATION REPORT
# ----------------------------------------------------

st.subheader("Classification Report")

report = classification_report(

    y_test,

    y_pred,

    output_dict=True

)

report_df = pd.DataFrame(report).transpose()

st.dataframe(

    report_df,

    use_container_width=True

)

st.divider()

# ----------------------------------------------------
# CONFUSION MATRIX
# ----------------------------------------------------

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test,y_pred)

cm_df = pd.DataFrame(

    cm,

    index=["Benign","Defacement","Malware","Phishing"],

    columns=["Benign","Defacement","Malware","Phishing"]

)

fig = px.imshow(

    cm_df,

    text_auto=True,

    color_continuous_scale="Blues"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# ----------------------------------------------------
# FEATURE IMPORTANCE
# ----------------------------------------------------

if hasattr(model,"feature_importances_"):

    st.subheader("Top 20 Important Features")

    importance = pd.DataFrame({

        "Feature":X.columns,

        "Importance":model.feature_importances_

    })

    importance = importance.sort_values(

        by="Importance",

        ascending=False

    ).head(20)

    fig = px.bar(

        importance,

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance"

    )

    fig.update_layout(

        yaxis=dict(categoryorder="total ascending")

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

else:

    st.info("Feature importance not available for this model.")