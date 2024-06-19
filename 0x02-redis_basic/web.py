#!/usr/bin/env python3
'''module with tools'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''module level redis instance'''


def data_cacher(method:Callable) -> Callable:
    '''cahce the output'''
    @wraps(method)
    def invoker(url) -> str:
        '''the wrapper function'''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''return the content of url'''
    return requests.get(url).text
