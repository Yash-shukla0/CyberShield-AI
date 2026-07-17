import joblib
import pandas as pd
from pathlib import Path

MODEL = joblib.load("models/best_model.pkl")
FEATURE_COLUMNS = joblib.load("models/feature_columns.pkl")


class URLExplainer:

    def __init__(self):
        self.model = MODEL

    def explain(self, feature_dict):

        df = pd.DataFrame([feature_dict])
        df = df.reindex(columns=FEATURE_COLUMNS, fill_value=0)

        importances = self.model.feature_importances_

        explanation = pd.DataFrame({
            "Feature": FEATURE_COLUMNS,
            "Importance": importances,
            "Value": df.iloc[0].values
        })

        explanation = explanation.sort_values(
            by="Importance",
            ascending=False
        )

        return explanation.head(10)