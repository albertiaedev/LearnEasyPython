# The _functools module provides classes and functions for working with functions, such as caching and partial application.

import _functools

@functools.lru_cache()
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))