"""
=========================================================
CyberShield AI
Lexical Feature Extraction

Author : Yash Shukla
=========================================================
"""

import math
import re
from collections import Counter
from urllib.parse import urlparse


class LexicalFeatureExtractor:
    """
    Extract lexical features from a URL.
    """

    def __init__(self, url: str):

        self.url = url.strip()

        self.parsed = urlparse(self.url)

    # ---------------------------------------------------
    # BASIC FEATURES
    # ---------------------------------------------------

    def url_length(self):
        return len(self.url)

    def hostname(self):
        return self.parsed.netloc

    def domain_length(self):
        return len(self.hostname())

    def path_length(self):
        return len(self.parsed.path)

    def query_length(self):
        return len(self.parsed.query)

    # ---------------------------------------------------
    # CHARACTER COUNTS
    # ---------------------------------------------------

    def dot_count(self):
        return self.url.count(".")

    def slash_count(self):
        return self.url.count("/")

    def hyphen_count(self):
        return self.url.count("-")

    def underscore_count(self):
        return self.url.count("_")

    def question_count(self):
        return self.url.count("?")

    def equal_count(self):
        return self.url.count("=")

    def ampersand_count(self):
        return self.url.count("&")

    def at_count(self):
        return self.url.count("@")

    def percent_count(self):
        return self.url.count("%")

    def hash_count(self):
        return self.url.count("#")

    # ---------------------------------------------------
    # CHARACTER TYPES
    # ---------------------------------------------------

    def digit_count(self):
        return sum(c.isdigit() for c in self.url)

    def letter_count(self):
        return sum(c.isalpha() for c in self.url)

    def special_character_count(self):

        return len(
            re.findall(
                r"[^A-Za-z0-9]",
                self.url
            )
        )

    # ---------------------------------------------------
    # RATIOS
    # ---------------------------------------------------

    def digit_ratio(self):

        length = len(self.url)

        if length == 0:
            return 0

        return self.digit_count() / length

    def letter_ratio(self):

        length = len(self.url)

        if length == 0:
            return 0

        return self.letter_count() / length

    def special_character_ratio(self):

        length = len(self.url)

        if length == 0:
            return 0

        return self.special_character_count() / length

    # ---------------------------------------------------
    # HTTPS
    # ---------------------------------------------------

    def uses_https(self):

        return int(self.parsed.scheme == "https")

    # ---------------------------------------------------
    # IP ADDRESS
    # ---------------------------------------------------

    def contains_ip(self):

        pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

        return int(
            re.match(
                pattern,
                self.hostname()
            ) is not None
        )

    # ---------------------------------------------------
    # SUSPICIOUS KEYWORDS
    # ---------------------------------------------------

    def suspicious_keyword_count(self):

        keywords = [

            "login",
            "verify",
            "update",
            "secure",
            "signin",
            "bank",
            "account",
            "password",
            "confirm",
            "wallet",
            "paypal",
            "bitcoin"

        ]

        url = self.url.lower()

        count = 0

        for word in keywords:

            if word in url:
                count += 1

        return count

    # ---------------------------------------------------
    # SHANNON ENTROPY
    # ---------------------------------------------------

    def entropy(self):

        if not self.url:
            return 0

        counts = Counter(self.url)

        probabilities = [
            c / len(self.url)
            for c in counts.values()
        ]

        return -sum(
            p * math.log2(p)
            for p in probabilities
        )

    # ---------------------------------------------------
    # FEATURE VECTOR
    # ---------------------------------------------------

    def extract(self):

        return {

            "url_length": self.url_length(),

            "domain_length": self.domain_length(),

            "path_length": self.path_length(),

            "query_length": self.query_length(),

            "dot_count": self.dot_count(),

            "slash_count": self.slash_count(),

            "hyphen_count": self.hyphen_count(),

            "underscore_count": self.underscore_count(),

            "question_count": self.question_count(),

            "equal_count": self.equal_count(),

            "ampersand_count": self.ampersand_count(),

            "at_count": self.at_count(),

            "percent_count": self.percent_count(),

            "hash_count": self.hash_count(),

            "digit_count": self.digit_count(),

            "letter_count": self.letter_count(),

            "special_character_count": self.special_character_count(),

            "digit_ratio": self.digit_ratio(),

            "letter_ratio": self.letter_ratio(),

            "special_character_ratio": self.special_character_ratio(),

            "uses_https": self.uses_https(),

            "contains_ip": self.contains_ip(),

            "suspicious_keyword_count": self.suspicious_keyword_count(),

            "entropy": self.entropy()

        }