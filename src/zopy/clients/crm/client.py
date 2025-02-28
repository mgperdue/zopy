from zopy.auth.oauth import OAuthHandler
from zopy.network.request import RequestHandler


class CRMClient:
    """Handles authentication and API requests for Zoho CRM."""

    def __init__(self):
        self.access_token = None

    def authenticate(self):
        """Authenticates and stores the access token."""
        self.access_token = OAuthHandler.get_access_token()

    def get_leads(self):
        """Fetches leads from Zoho CRM."""
        if not self.access_token:
            raise ValueError("Client not authenticated. Call `authenticate()` first.")
        return RequestHandler.get("crm/v2/Leads")
