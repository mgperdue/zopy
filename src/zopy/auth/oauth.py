import requests
import logging

logger = logging.getLogger("zopy.auth")


class OAuth:
    AUTH_URL = "https://accounts.zoho.com/oauth/v2/auth"
    TOKEN_URL = "https://accounts.zoho.com/oauth/v2/token"

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_auth_url(self, scope="ZohoCRM.modules.ALL"):
        """Generate OAuth authorization URL."""
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": scope,
            "access_type": "offline",
        }
        return f"{self.AUTH_URL}?{'&'.join(f'{k}={v}' for k, v in params.items())}"

    def exchange_code_for_token(self, code):
        """Exchange authorization code for access and refresh tokens."""
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
            "code": code,
        }
        response = requests.post(self.TOKEN_URL, data=payload)
        return response.json()

    def refresh_access_token(self, refresh_token):
        """Refresh expired access token."""
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        response = requests.post(self.TOKEN_URL, data=payload)
        return response.json()
