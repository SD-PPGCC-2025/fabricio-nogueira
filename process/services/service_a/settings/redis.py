from functools import cache

import redis

from settings import settings


@cache
class Redis:
    """
    Singleton redis instance
    """

    def __init__(self):
        self.instance = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True
        )
