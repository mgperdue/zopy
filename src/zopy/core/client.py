import requests

from zopy.auth.oauth import OAuthHandler


class APIClient:
    """Handles API requests and authentication."""

    BASE_URL = "https://www.zohoapis.com"

    def __init__(self):
        self.access_token = OAuthHandler.get_access_token()

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}

    def get(self, endpoint, params=None):
        """Performs a GET request."""
        response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=self._get_headers(), params=params)
        return response.json()

    def post(self, endpoint, data):
        """Performs a POST request."""
        response = requests.post(f"{self.BASE_URL}/{endpoint}", headers=self._get_headers(), json=data)
        return response.json()
