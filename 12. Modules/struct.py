# The _struct module provides functions for packing and unpacking binary data.

import _struct

packed_data = _struct.pack(">i", 1234567890)

unpacked_data = _struct.unpack(">i", packed_data)

print(unpacked_data)