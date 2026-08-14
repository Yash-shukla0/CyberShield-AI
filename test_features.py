import pandas as pd
import joblib

MODEL = joblib.load("models/best_model.pkl")

FEATURE_COLUMNS = joblib.load(
    "models/feature_columns.pkl"
)

df = pd.read_parquet(
    "data/processed/processed_dataset.parquet"
)

# Pick 10 benign samples
benign = df[df["label"] == 0].sample(
    10,
    random_state=42
)

X = benign.drop(
    columns=["url", "type", "label"]
)

X = X.reindex(columns=FEATURE_COLUMNS)

predictions = MODEL.predict(X)

probabilities = MODEL.predict_proba(X)

print("=" * 70)
print("BENIGN TRAINING DATA TEST")
print("=" * 70)

for i in range(len(benign)):

    print("\nURL:", benign.iloc[i]["url"])

    print(
        "Actual:",
        benign.iloc[i]["type"],
        "(label =", benign.iloc[i]["label"], ")"
    )

    print(
        "Predicted:",
        predictions[i]
    )

    print(
        "Probabilities:",
        probabilities[i]
    )