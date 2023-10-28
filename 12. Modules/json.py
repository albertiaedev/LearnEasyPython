# The _json module provides classes and functions for encoding and decoding JSON data.

import _json

json_string = json.dumps({"name": "Alice"})

print(json_string)

json_object = json.loads(json_string)

print(json_object)