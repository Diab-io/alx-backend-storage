#!/usr/bin/env python3
"""
module containing a cache class
"""

import redis
import uuid
from typing import Union


class Cache:
    """ class that stores data into the redis mem """
    def __init__(self) -> None:
        """ clears the db on every instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """
            This metohod stores the data with the generated key
            args:
                data - data that is to be added
        """
        generated_key = str(uuid.uuid4())
        self._redis.set({generated_key: data})
        return generated_key