# Functions that modify other functions (wrap them) without changing their code.
#  Useful for logging, auth, timing, etc.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

slow_sum(10_000_000)




# Key idea: higher-order function returning a wrapper that preserves metadata with functools.wraps if desired.