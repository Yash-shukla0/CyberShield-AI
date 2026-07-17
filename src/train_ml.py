"""
=========================================================
CyberShield AI
Machine Learning Training Pipeline

Author : Yash Shukla
=========================================================
"""
import os
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


import matplotlib.pyplot as plt

import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

# -------------------------------------------------------
# PATHS
# -------------------------------------------------------

DATA_PATH = Path("data/processed/processed_dataset.parquet")

MODEL_DIR = Path("models")

MODEL_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# LOAD DATA
# -------------------------------------------------------

print("=" * 60)
print("Loading Processed Dataset...")
print("=" * 60)

df = pd.read_parquet(DATA_PATH)
# Remove rows with missing feature values
df = df.dropna().reset_index(drop=True)

print(f"\nDataset after removing invalid rows: {df.shape}")

print(f"\nDataset Shape : {df.shape}")

print("\nColumns:")

print(df.columns.tolist())

print("\nClass Distribution:")

print(df["label"].value_counts())

# -------------------------------------------------------
# FEATURES & TARGET
# -------------------------------------------------------

DROP_COLUMNS = [
    "url",
    "type",
    "label"
]

X = df.drop(columns=DROP_COLUMNS)

y = df["label"]

print("\nNumber of Features :", X.shape[1])

print("Number of Samples :", X.shape[0])

# -------------------------------------------------------
# TRAIN TEST SPLIT
# -------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# -------------------------------------------------------
# SAVE FEATURE COLUMNS
# -------------------------------------------------------

joblib.dump(
    X.columns.tolist(),
    MODEL_DIR / "feature_columns.pkl"
)

print("\nFeature Columns Saved.")

# -------------------------------------------------------
# RANDOM FOREST MODEL
# -------------------------------------------------------

print("\n" + "=" * 60)
print("Training Random Forest...")
print("=" * 60)

rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

print("Training Completed.")

# -------------------------------------------------------
# PREDICTIONS
# -------------------------------------------------------

y_pred = rf_model.predict(X_test)

# -------------------------------------------------------
# METRICS
# -------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

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

print("\nModel Performance")
print("-" * 40)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nClassification Report\n")

print(classification_report(y_test, y_pred))

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test, y_pred))
# -------------------------------------------------------
# SAVE MODEL
# -------------------------------------------------------

joblib.dump(
    rf_model,
    MODEL_DIR / "random_forest.pkl"
)

print("\nRandom Forest Model Saved!")

print("\n" + "=" * 60)
print("Training XGBoost...")
print("=" * 60)

xgb_model = XGBClassifier(
    objective="multi:softprob",
    num_class=4,
    n_estimators=300,
    max_depth=8,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="mlogloss"
)

xgb_model.fit(X_train, y_train)

y_pred_xgb = xgb_model.predict(X_test)

accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
precision_xgb = precision_score(y_test, y_pred_xgb, average="weighted")
recall_xgb = recall_score(y_test, y_pred_xgb, average="weighted")
f1_xgb = f1_score(y_test, y_pred_xgb, average="weighted")

print("\nXGBoost Performance")
print("-" * 40)
print(f"Accuracy : {accuracy_xgb:.4f}")
print(f"Precision: {precision_xgb:.4f}")
print(f"Recall   : {recall_xgb:.4f}")
print(f"F1 Score : {f1_xgb:.4f}")

print("\nClassification Report\n")
print(classification_report(y_test, y_pred_xgb))

# -------------------------------------------------------
# SAVE REPORTS
# -------------------------------------------------------

report = classification_report(y_test, y_pred_xgb)

with open("reports/classification_report.txt", "w") as f:
    f.write(report)

cm = confusion_matrix(y_test, y_pred_xgb)

plt.figure(figsize=(7, 6))

plt.imshow(cm)

plt.colorbar()

plt.xticks([0,1,2,3], ["Benign","Defacement","Malware","Phishing"])
plt.yticks([0,1,2,3], ["Benign","Defacement","Malware","Phishing"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, str(cm[i, j]),
                 ha="center",
                 va="center")

plt.tight_layout()

plt.savefig("reports/confusion_matrix.png", dpi=300)

plt.close()

print("\nReports Saved!")

metrics = f"""
Model : XGBoost

Accuracy  : {accuracy_xgb:.4f}
Precision : {precision_xgb:.4f}
Recall    : {recall_xgb:.4f}
F1 Score  : {f1_xgb:.4f}
"""

with open("reports/model_metrics.txt", "w") as f:
    f.write(metrics)

if f1_xgb > f1:
    best_model = xgb_model
    best_name = "XGBoost"
else:
    best_model = rf_model
    best_name = "Random Forest"

joblib.dump(best_model, MODEL_DIR / "best_model.pkl")

print(f"\nBest Model: {best_name}")