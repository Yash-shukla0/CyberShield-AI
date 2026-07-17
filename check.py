import pandas as pd

df = pd.read_csv("data/raw/malicious_phish.csv")

for u in [
    "google.com",
    "http://google.com",
    "https://google.com",
]:
    print("\n", u)
    print(df[df["url"] == u])