import pandas as pd

# Change the path if your file has a different name
df = pd.read_csv("data/raw/phishing_urls.csv")

print("Columns:")
print(df.columns.tolist())

print("\nUnique Labels:")
print(df["label"].unique())

print("\nLabel Counts:")
print(df["label"].value_counts())