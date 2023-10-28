# The _pickle module provides functions for serializing and deserializing Python objects.

import _pickle

# Serialize an object
serialized_object = _pickle.dumps({"name": "Alice"})

# Deserialize the object
deserialized_object = _pickle.loads(serialized_object)

# Print the object
print(deserialized_object)