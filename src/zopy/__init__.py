"""
ZoPy: A Python client for Zoho APIs.

This package provides authentication, request handling, and API clients
for various Zoho applications, including CRM, Projects, Books, Desk, and Creator.
"""

__version__ = "0.1.0"

from .auth import oauth, token_manager

# Application-specific API clients


# Define the public API
__all__ = [
    "oauth",
    "token_manager",
]
