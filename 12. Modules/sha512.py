# The _sha512 module provides functions for calculating SHA512 hashes.

import _sha512

hash = _sha512.new()

hash.update("Hello, world!".encode())

print(hash.hexdigest())