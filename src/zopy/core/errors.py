class APIError(Exception):
    """Base exception for all API errors."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

class NotFoundError(APIError):
    """Exception for 404 errors."""
    def __init__(self, message="Resource not found"):
        super().__init__(message, status_code=404)

class ServerError(APIError):
    """Exception for 5xx server errors."""
    def __init__(self, message="Internal server error"):
        super().__init__(message, status_code=500)

class AuthenticationError(APIError):
    """Exception for authentication failures."""
    def __init__(self, message="Authentication failed"):
        super().__init__(message, status_code=401)

def handle_errors(response):
    """Processes API response and raises appropriate errors."""
    if response.status_code == 404:
        raise NotFoundError(f"Resource not found: {response.url}")
    elif response.status_code >= 500:
        raise ServerError()
    elif response.status_code == 401:
        raise AuthenticationError()
    return response.json()
