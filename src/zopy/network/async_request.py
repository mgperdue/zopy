import httpx

from zopy.core.errors import handle_errors
from zopy.network.headers import get_default_headers


class AsyncRequestHandler:
    """Handles asynchronous HTTP requests for Zoho APIs."""

    BASE_URL = "https://www.zohoapis.com"

    @staticmethod
    async def send_request(method, endpoint, params=None, json=None):
        """Handles async API requests with error handling."""
        url = f"{AsyncRequestHandler.BASE_URL}/{endpoint}"
        headers = get_default_headers()

        async with httpx.AsyncClient() as client:
            response = await client.request(
                method, url, params=params, json=json, headers=headers
            )
        return handle_errors(response)

    @staticmethod
    async def get(endpoint, params=None):
        return await AsyncRequestHandler.send_request("GET", endpoint, params=params)

    @staticmethod
    async def post(endpoint, data):
        return await AsyncRequestHandler.send_request("POST", endpoint, json=data)

    @staticmethod
    async def put(endpoint, data):
        return await AsyncRequestHandler.send_request("PUT", endpoint, json=data)

    @staticmethod
    async def delete(endpoint):
        return await AsyncRequestHandler.send_request("DELETE", endpoint)
