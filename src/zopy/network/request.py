import requests

from headers import get_default_headers
from retry import retry_request
from zopy.core.errors import handle_errors
from zopy.core.logging import log_request, log_response, log_error


class RequestHandler:
    """Handles all HTTP requests for Zoho APIs."""

    BASE_URL = "https://www.zohoapis.com"

    @staticmethod
    def send_request(method, endpoint, params=None, json=None):
        """Handles API requests with logging, retries, and error handling."""
        url = f"{RequestHandler.BASE_URL}/{endpoint}"
        headers = get_default_headers()

        log_request(method, url)
        try:
            response = retry_request(
                lambda: requests.request(
                    method, url, params=params, json=json, headers=headers
                )
            )
            log_response(response)
            return handle_errors(response)
        except Exception as e:
            log_error(e)
            raise

    @staticmethod
    def get(endpoint, params=None):
        return RequestHandler.send_request("GET", endpoint, params=params)

    @staticmethod
    def post(endpoint, data):
        return RequestHandler.send_request("POST", endpoint, json=data)

    @staticmethod
    def put(endpoint, data):
        return RequestHandler.send_request("PUT", endpoint, json=data)

    @staticmethod
    def delete(endpoint):
        return RequestHandler.send_request("DELETE", endpoint)
