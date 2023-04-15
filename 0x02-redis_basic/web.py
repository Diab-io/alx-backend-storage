#!/usr/bin/env python3

""" caching requests """

import requests
import redis
from typing import Callable
from functools import wraps


def cache_count(method: Callable) -> Callable:
    """
    stores the response got from the request and
    the number of times the request was made to the url
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        redis_server = redis.Redis()
        redis_server.incr(f"count:{url}")
        page_cache = redis_server.get(f'{url}')
        if page_cache:
            return page_cache.decode("utf-8")
        res = method(url)
        redis_server.set(url, res, 10)
        return res
    return wrapper


@cache_count
def get_page(url: str) -> str:
    """ send an http request to the url """
    res = requests.get(url)
    return res.text
