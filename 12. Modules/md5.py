# The _md5 module provides functions for calculating MD5 hashes.

import _md5

hash = _md5.new()

hash.update("Hello, world!".encode())

print(hash.hexdigest())