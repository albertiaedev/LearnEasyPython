# The _codecs module provides classes and functions for encoding and decoding data between different character encodings.

import _codecs

encoded_string = _codecs.encode("Hello, world!", "utf-8")

print(encoded_string)

decoded_string = _codecs.decode(encoded_string, "utf-8")

print(decoded_string)