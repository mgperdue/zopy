"""
ZoPy: A Python client for Zoho APIs.

This package provides authentication, request handling, and API clients
for various Zoho applications, including CRM, Projects, Books, Desk, and Creator.
"""

__version__ = "0.1.0"

# Import core functionality
from .auth import oauth, token_manager
from .core.config import CONFIG
from .core.base_client import BaseZohoClient
from .monitoring import quota_manager, performance_tracker
from .network.api_client import APIClient

# Application-specific API clients
from .applications.crm.client import CRMClient
from .applications.projects.client import ProjectsClient

# Define the public API
__all__ = [
    "oauth",
    "token_manager",
    "BaseZohoClient",
    "CONFIG",
    "quota_manager",
    "performance_tracker",
    "APIClient",
    "CRMClient",
    "ProjectsClient",
]
