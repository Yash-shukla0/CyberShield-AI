import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

print("=" * 60)
print("Loading Model...")
print("=" * 60)

model = joblib.load("models/best_model.pkl")
features = joblib.load("models/feature_columns.pkl")

print("Model Loaded.")

# ----------------------------------------------------
# FEATURE IMPORTANCE
# ----------------------------------------------------

if hasattr(model, "feature_importances_"):

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nTop 20 Features\n")
    print(importance.head(20))

    plt.figure(figsize=(10,8))

    plt.barh(
        importance.head(20)["Feature"][::-1],
        importance.head(20)["Importance"][::-1]
    )

    plt.xlabel("Importance")
    plt.title("Top 20 Feature Importance")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            REPORT_DIR,
            "feature_importance.png"
        ),
        dpi=300
    )

    plt.show()

    print("\nFeature Importance Saved.")

else:

    print("Model does not support feature importance.")