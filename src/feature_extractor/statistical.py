"""
=========================================================
CyberShield AI
Statistical Feature Extraction

Author : Yash Shukla
=========================================================
"""

import re
from urllib.parse import urlparse


class StatisticalFeatureExtractor:
    """
    Extract statistical features from a URL.
    """

    def __init__(self, url: str):

        self.url = url.strip()

        self.parsed = urlparse(url)

    # ---------------------------------------------------
    # BASIC COUNTS
    # ---------------------------------------------------

    def letters(self):
        return sum(c.isalpha() for c in self.url)

    def digits(self):
        return sum(c.isdigit() for c in self.url)

    def specials(self):
        return len(re.findall(r'[^A-Za-z0-9]', self.url))

    # ---------------------------------------------------
    # RATIOS
    # ---------------------------------------------------

    def digit_letter_ratio(self):

        letters = self.letters()

        if letters == 0:
            return 0

        return self.digits() / letters

    def special_letter_ratio(self):

        letters = self.letters()

        if letters == 0:
            return 0

        return self.specials() / letters

    def uppercase_ratio(self):

        length = len(self.url)

        if length == 0:
            return 0

        upper = sum(c.isupper() for c in self.url)

        return upper / length

    # ---------------------------------------------------
    # LONGEST TOKEN
    # ---------------------------------------------------

    def longest_token_length(self):

        tokens = re.split(r"[./?=&:_-]", self.url)

        if not tokens:
            return 0

        return max(len(t) for t in tokens)

    # ---------------------------------------------------
    # AVERAGE TOKEN LENGTH
    # ---------------------------------------------------

    def average_token_length(self):

        tokens = [
            t for t in re.split(r"[./?=&:_-]", self.url)
            if t
        ]

        if not tokens:
            return 0

        return sum(len(t) for t in tokens) / len(tokens)

    # ---------------------------------------------------
    # CHARACTER DIVERSITY
    # ---------------------------------------------------

    def character_diversity(self):

        if len(self.url) == 0:
            return 0

        return len(set(self.url)) / len(self.url)

    # ---------------------------------------------------
    # CONSECUTIVE DIGITS
    # ---------------------------------------------------

    def consecutive_digits(self):

        groups = re.findall(r"\d+", self.url)

        if not groups:
            return 0

        return max(len(g) for g in groups)

    # ---------------------------------------------------
    # CONSECUTIVE SPECIAL CHARACTERS
    # ---------------------------------------------------

    def consecutive_specials(self):

        groups = re.findall(r"[^A-Za-z0-9]+", self.url)

        if not groups:
            return 0

        return max(len(g) for g in groups)

    # ---------------------------------------------------
    # URL COMPLEXITY SCORE
    # ---------------------------------------------------

    def complexity_score(self):

        score = 0

        score += self.specials()
        score += self.digits()

        score += self.url.count("-")
        score += self.url.count("@")
        score += self.url.count("?")
        score += self.url.count("=")
        score += self.url.count("&")

        return score

    # ---------------------------------------------------
    # FEATURE VECTOR
    # ---------------------------------------------------

    def extract(self):

        return {

            "digit_letter_ratio": self.digit_letter_ratio(),

            "special_letter_ratio": self.special_letter_ratio(),

            "uppercase_ratio": self.uppercase_ratio(),

            "longest_token_length": self.longest_token_length(),

            "average_token_length": self.average_token_length(),

            "character_diversity": self.character_diversity(),

            "consecutive_digits": self.consecutive_digits(),

            "consecutive_specials": self.consecutive_specials(),

            "complexity_score": self.complexity_score()

        }