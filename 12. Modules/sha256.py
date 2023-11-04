# The _sha256 module provides functions for calculating SHA256 hashes.

import _sha256

hash = _sha256.new()

hash.update("Hello, world!".encode())

print(hash.hexdigest())