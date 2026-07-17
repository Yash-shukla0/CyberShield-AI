"""
=========================================================
CyberShield AI
Data Preprocessing Pipeline

Author : Yash Shukla
=========================================================
"""
import joblib
import time
from pathlib import Path

import pandas as pd
from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder

from src.feature_extractor import URLFeatureExtractor

# -------------------------------------------------------
# PATHS
# -------------------------------------------------------

RAW_DATASET = Path("data/raw/malicious_phish.csv")

OUTPUT_DIR = Path("data/processed")

OUTPUT_FILE = OUTPUT_DIR / "processed_dataset.parquet"

# -------------------------------------------------------
# DEVELOPMENT MODE
# -------------------------------------------------------

DEVELOPMENT_MODE = False

SAMPLE_SIZE = 10000


# -------------------------------------------------------
# LABEL ENCODER
# -------------------------------------------------------

label_encoder = LabelEncoder()

# -------------------------------------------------------
# PREPROCESS CLASS
# -------------------------------------------------------

class DataPreprocessor:

    def __init__(self):

        self.df = None

    # ---------------------------------------------------
    # LOAD DATASET
    # ---------------------------------------------------

    def load_dataset(self):

        print("=" * 60)
        print("Loading Dataset...")
        print("=" * 60)

        self.df = pd.read_csv(RAW_DATASET)

        print(f"Dataset Shape : {self.df.shape}")

        print("\nColumns")

        print(self.df.columns.tolist())

        print("\nClass Distribution")

        print(self.df["type"].value_counts())

    # ---------------------------------------------------
    # VALIDATE
    # ---------------------------------------------------

    def validate_columns(self):

        required = ["url", "type"]

        for column in required:

            if column not in self.df.columns:

                raise Exception(
                    f"Missing Column : {column}"
                )

        print("\nRequired columns verified.")

    # ---------------------------------------------------
    # CLEAN URL
    # ---------------------------------------------------

    def clean_urls(self):

        print("\nCleaning URLs...")

        self.df["url"] = (

            self.df["url"]

            .astype(str)

            .str.strip()

        )

        self.df = self.df[

            self.df["url"] != ""

        ]

        self.df = self.df.drop_duplicates(
            subset=["url"]
        )

        self.df = self.df.reset_index(drop=True)

        print("Cleaning completed.")

    # ---------------------------------------------------
    # LABEL ENCODING
    # ---------------------------------------------------

    def encode_labels(self):

        print("\nEncoding Labels...")

        self.df["label"] = label_encoder.fit_transform(
            self.df["type"]
        )

        mapping = dict(

            zip(

                label_encoder.classes_,

                label_encoder.transform(
                    label_encoder.classes_
                )

            )

        )

        print("\nLabel Mapping")

        print(mapping)
    # ---------------------------------------------------
    # FEATURE EXTRACTION
    # ---------------------------------------------------

    def extract_features(self):

        print("\n" + "=" * 60)
        print("Extracting Features...")
        print("=" * 60)

        # Development Mode
        if DEVELOPMENT_MODE:

            self.df = self.df.sample(
                n=SAMPLE_SIZE,
                random_state=42
            ).reset_index(drop=True)

            print(f"Development Mode Enabled")
            print(f"Processing {len(self.df)} URLs...\n")

        feature_rows = []

        for url in tqdm(self.df["url"]):

            try:

                extractor = URLFeatureExtractor(url)

                feature_rows.append(
                    extractor.extract_dict()
                )

            except Exception as e:

                print(f"Error processing URL: {url}")
                print(e)

                feature_rows.append({})

        feature_df = pd.DataFrame(feature_rows)

        self.df = pd.concat(
            [
                self.df.reset_index(drop=True),
                feature_df.reset_index(drop=True)
            ],
            axis=1
        )

        print("\nFeature Extraction Completed.")

    # ---------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------

    def summary(self):

        print("\nDataset Ready")

        print(self.df.head())

        print()

        print(self.df.info())
    # ---------------------------------------------------
    # SAVE DATASET
    # ---------------------------------------------------

    def save_dataset(self):

        print("\nSaving Processed Dataset...")

        OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        # Save complete dataset
        self.df.to_parquet(
            OUTPUT_FILE,
            index=False
        )

        # Save label encoder
        joblib.dump(
            label_encoder,
            OUTPUT_DIR / "label_encoder.pkl"
        )

        print("Dataset Saved Successfully!")

        print(f"\nLocation : {OUTPUT_FILE}")

# -------------------------------------------------------
# MAIN
# -------------------------------------------------------

if __name__ == "__main__":

    start = time.time()

    processor = DataPreprocessor()

    processor.load_dataset()

    processor.validate_columns()

    processor.clean_urls()

    processor.encode_labels()

    processor.extract_features()

    processor.summary()

    processor.save_dataset()

    end = time.time()

    print(f"\nFinished in {end-start:.2f} seconds.")