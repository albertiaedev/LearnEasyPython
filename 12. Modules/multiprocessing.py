# The _multiprocessing module provides classes and functions for implementing parallelism in Python.

import _multiprocessing

def square(x):
    return x * x

# Create a pool of workers
pool = _multiprocessing.Pool()

# Map the square function to all the numbers in the list
results = pool.map(square, [1, 2, 3, 4])

# Print the results
print(results)