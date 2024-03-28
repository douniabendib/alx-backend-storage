#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    '''declares a Cache redis class'''
    def __init__(self):
        '''upon init to store an instance and flush'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    """@call_history
    @count_calls
    """
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''takes a data argument and returns a string'''
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey
