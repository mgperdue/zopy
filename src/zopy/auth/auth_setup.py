import webbrowser
from zopy.auth.oauth import OAuth
from zopy.auth.token_manager import TokenManager


def authenticate():
    """Interactive CLI for first-time authentication."""
    client_id = input("Enter your Zoho Client ID: ")
    client_secret = input("Enter your Zoho Client Secret: ")
    redirect_uri = input("Enter your Redirect URI: ")

    oauth = OAuth(client_id, client_secret, redirect_uri)
    auth_url = oauth.get_auth_url()

    print(f"Open this URL in your browser and log in:\n{auth_url}")
    webbrowser.open(auth_url)

    code = input("Enter the authorization code from Zoho: ")
    tokens = oauth.exchange_code_for_token(code)

    TokenManager.save_tokens(tokens)
    print("Authentication successful! Tokens saved.")


if __name__ == "__main__":
    authenticate()
