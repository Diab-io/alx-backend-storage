#!/usr/bin/env python3
"""
module containing a cache class
"""

import redis
import uuid
from typing import Union, Optional, Callable
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ this counts the number of times a method is called """
    incr_key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """Decorator that counts the no of times the callable method is run"""
        self._redis.incr(incr_key)
        return method(self, *args, **kwargs)
    return counter


class Cache:
    """ class that stores data into the redis mem """
    def __init__(self) -> None:
        """ clears the db on every instance """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[int, str, bytes, float]) -> str:
        """
            This metohod stores the data with the generated key
            args:
                data - data that is to be added
        """
        generated_key = str(uuid.uuid4())
        self._redis.set(generated_key, data)
        return generated_key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        This method gets the value of the passed key
        and can be used in a callable func
        """
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, byte_data: bytes) -> str:
        """ method that converts byte to string """
        return byte_data.decode("utf-8")

    def get_int(self, byte_data: bytes) -> int:
        """ method that converts byte to int """
        return int.from_bytes(byte_data, sys.byteorder)
