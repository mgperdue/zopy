from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))  # Retries up to 3 times
def retry_request(func):
    """Retries a given function (for handling network failures)."""
    return func()
