# The _tracemalloc module provides functions for tracing memory allocations.

import _tracemalloc

_tracemalloc.start()

# Do some memory allocations

_tracemalloc.stop()

# Print the memory allocations
print(_tracemalloc.get_traced_memory())