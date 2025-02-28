import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_request(method, url):
    """Logs API request details."""
    logging.info(f"API Request: {method} {url}")

def log_response(response):
    """Logs API response details."""
    logging.info(f"API Response [{response.status_code}]: {response.text}")

def log_error(error):
    """Logs error messages."""
    logging.error(f"API Error: {error}")
