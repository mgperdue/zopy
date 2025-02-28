import time


class RateLimiter:
    """Enforces API rate limits."""

    RATE_LIMIT = 10  # Max 10 requests per second
    last_request_time = 0

    @staticmethod
    def enforce_limit():
        """Waits if rate limit is exceeded."""
        now = time.time()
        if now - RateLimiter.last_request_time < (1 / RateLimiter.RATE_LIMIT):
            time.sleep(1 / RateLimiter.RATE_LIMIT)
        RateLimiter.last_request_time = now
