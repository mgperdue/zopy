import json
import time

import requests

TOKEN_FILE = "zopy_token.json"
ZOHO_AUTH_URL = "https://accounts.zoho.com/oauth/v2/token"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REFRESH_TOKEN = "your_refresh_token"


class OAuthHandler:
    """Handles OAuth 2.0 authentication and token refreshing."""

    @staticmethod
    def get_access_token():
        """Retrieves a valid access token, refreshing it if needed."""
        token_data = OAuthHandler._load_token()
        if time.time() > token_data["expires_at"]:
            return OAuthHandler.refresh_access_token()
        return token_data["access_token"]

    @staticmethod
    def refresh_access_token():
        """Refreshes the OAuth token when expired."""
        payload = {
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "refresh_token",
        }
        response = requests.post(ZOHO_AUTH_URL, data=payload).json()
        OAuthHandler._save_token(response["access_token"], response["expires_in"])
        return response["access_token"]

    @staticmethod
    def _load_token():
        """Loads the stored token from file."""
        try:
            with open(TOKEN_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"access_token": None, "expires_at": 0}

    @staticmethod
    def _save_token(access_token, expires_in):
        """Saves the token securely."""
        token_data = {
            "access_token": access_token,
            "expires_at": time.time() + expires_in,
        }
        with open(TOKEN_FILE, "w") as file:
            json.dump(token_data, file)
