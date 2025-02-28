import json
import os

from zopy.core.logging_config import logger

TOKEN_FILE = "tokens.json"

# TODO: Add encryption support to store tokens more securely
# TODO: Implement an environment variable option instead of using tokens.json
# TODO: Refine CLI prompts for a smoother user experience


class TokenManager:
    @staticmethod
    def save_tokens(tokens):
        """Save access and refresh tokens to a file."""
        with open(TOKEN_FILE, "w") as f:
            json.dump(tokens, f)

    @staticmethod
    def load_tokens():
        """Load saved tokens from a file."""
        if not os.path.exists(TOKEN_FILE):
            logger.warning("No tokens found. Please authenticate.")
            return None
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def get_access_token():
        """Retrieve the current access token."""
        tokens = TokenManager.load_tokens()
        return tokens.get("access_token") if tokens else None

    @staticmethod
    def refresh_access_token():
        """Refresh the access token using stored refresh token."""
        tokens = TokenManager.load_tokens()
        if not tokens or "refresh_token" not in tokens:
            logger.error("No refresh token found.")
            return None
        from zopy.auth.oauth import OAuth  # Avoid circular import

        oauth = OAuth(
            client_id="your_client_id",
            client_secret="your_client_secret",
            redirect_uri="your_redirect_uri",
        )
        new_tokens = oauth.refresh_access_token(tokens["refresh_token"])
        TokenManager.save_tokens(new_tokens)
        return new_tokens.get("access_token")
