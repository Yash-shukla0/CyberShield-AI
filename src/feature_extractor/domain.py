"""
=========================================================
CyberShield AI
Domain Feature Extraction

Author : Yash Shukla
=========================================================
"""

from urllib.parse import urlparse

import tldextract


class DomainFeatureExtractor:
    """
    Extract domain-based features from a URL.
    """

    def __init__(self, url: str):

        self.url = url.strip()

        self.parsed = urlparse(self.url)

        self.extracted = tldextract.extract(self.url)

    # --------------------------------------------------
    # DOMAIN
    # --------------------------------------------------

    def domain(self):
        return self.extracted.domain

    def subdomain(self):
        return self.extracted.subdomain

    def suffix(self):
        return self.extracted.suffix

    # --------------------------------------------------
    # LENGTHS
    # --------------------------------------------------

    def subdomain_length(self):
        return len(self.subdomain())

    def suffix_length(self):
        return len(self.suffix())

    # --------------------------------------------------
    # SUBDOMAIN
    # --------------------------------------------------

    def subdomain_count(self):

        sub = self.subdomain()

        if sub == "":
            return 0

        return len(sub.split("."))

    # --------------------------------------------------
    # PORT
    # --------------------------------------------------

    def has_port(self):

        return int(self.parsed.port is not None)

    # --------------------------------------------------
    # SCHEME
    # --------------------------------------------------

    def scheme(self):

        return self.parsed.scheme

    def is_https(self):

        return int(self.scheme() == "https")

    # --------------------------------------------------
    # DOMAIN TOKENS
    # --------------------------------------------------

    def token_count(self):

        tokens = self.domain().split("-")

        return len(tokens)

    # --------------------------------------------------
    # SUSPICIOUS TLD
    # --------------------------------------------------

    def suspicious_tld(self):

        suspicious = {

            "zip",
            "country",
            "click",
            "link",
            "work",
            "gq",
            "tk",
            "ml",
            "cf",
            "ga",
            "xyz",
            "top",
            "buzz",
            "monster",
            "rest",
            "fit"
        }

        return int(
            self.suffix().lower() in suspicious
        )

    # --------------------------------------------------
    # DOMAIN STARTS WITH DIGIT
    # --------------------------------------------------

    def starts_with_digit(self):

        domain = self.domain()

        if len(domain) == 0:
            return 0

        return int(domain[0].isdigit())

    # --------------------------------------------------
    # HYPHEN IN DOMAIN
    # --------------------------------------------------

    def has_hyphen(self):

        return int("-" in self.domain())

    # --------------------------------------------------
    # DOMAIN IS LONG
    # --------------------------------------------------

    def long_domain(self):

        return int(len(self.domain()) > 20)

    # --------------------------------------------------
    # FEATURE VECTOR
    # --------------------------------------------------

    def extract(self):

        return {

            "subdomain_length": self.subdomain_length(),

            "suffix_length": self.suffix_length(),

            "subdomain_count": self.subdomain_count(),

            "has_port": self.has_port(),

            "is_https": self.is_https(),

            "domain_token_count": self.token_count(),

            "suspicious_tld": self.suspicious_tld(),

            "starts_with_digit": self.starts_with_digit(),

            "has_hyphen_domain": self.has_hyphen(),

            "long_domain": self.long_domain()

        }