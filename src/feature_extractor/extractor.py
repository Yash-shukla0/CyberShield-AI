"""
=========================================================
CyberShield AI
Master Feature Extractor

Author : Yash Shukla
=========================================================
"""

import pandas as pd

from src.feature_extractor.lexical import LexicalFeatureExtractor
from src.feature_extractor.domain import DomainFeatureExtractor
from src.feature_extractor.statistical import StatisticalFeatureExtractor

from urllib.parse import urlparse

class URLFeatureExtractor:
    """
    Master Feature Extractor

    Combines:
    1. Lexical Features
    2. Domain Features
    3. Statistical Features
    """

    def __init__(self, url: str):

        url = url.strip()

        if not url.startswith(("http://", "https://")):
            url = "http://" + url

        self.url = url

    # --------------------------------------------------
    # Dictionary
    # --------------------------------------------------

    def extract_dict(self):

        lexical = LexicalFeatureExtractor(self.url).extract()

        domain = DomainFeatureExtractor(self.url).extract()

        statistical = StatisticalFeatureExtractor(self.url).extract()

        features = {}

        features.update(lexical)
        features.update(domain)
        features.update(statistical)

        return features

    # --------------------------------------------------
    # DataFrame
    # --------------------------------------------------

    def extract_dataframe(self):

        return pd.DataFrame(
            [self.extract_dict()]
        )

    # --------------------------------------------------
    # Feature Names
    # --------------------------------------------------

    def feature_names(self):

        return list(
            self.extract_dict().keys()
        )

    # --------------------------------------------------
    # Number of Features
    # --------------------------------------------------

    def feature_count(self):

        return len(
            self.extract_dict()
        )


# ------------------------------------------------------
# Helper Function
# ------------------------------------------------------

def extract_features(url: str):

    """
    Returns a pandas DataFrame
    ready for ML prediction.
    """

    extractor = URLFeatureExtractor(url)

    return extractor.extract_dataframe()


# ------------------------------------------------------
# Example
# ------------------------------------------------------

if __name__ == "__main__":

    url = "https://secure-paypal-login.xyz/login"

    extractor = URLFeatureExtractor(url)

    df = extractor.extract_dataframe()

    print(df)

    print()

    print("Number of Features :")

    print(extractor.feature_count())