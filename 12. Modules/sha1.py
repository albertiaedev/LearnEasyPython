# The _sha1 module provides functions for calculating SHA1 hashes.

import _sha1

hash = _sha1.new()

hash.update("Hello, world!".encode())

print(hash.hexdigest())