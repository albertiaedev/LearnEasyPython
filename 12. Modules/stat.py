# The _stat module provides classes and functions for working with file statistics.

import _stat

stat = _stat.stat("myfile.txt")

print(stat.st_size)
print(stat.st_mtime)