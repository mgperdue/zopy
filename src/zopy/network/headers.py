from zopy.auth.oauth import OAuthHandler


def get_default_headers():
    """Returns standard headers with authorization token."""
    return {
        "Authorization": f"Bearer {OAuthHandler.get_access_token()}",
        "Content-Type": "application/json",
    }
