# The _collections module provides classes for implementing various data structures, such as dictionaries, sets, and queues.

import _collections

# Create a dictionary
dictionary = _collections.defaultdict(list)

# Add some items to the dictionary
dictionary["a"].append(1)
dictionary["b"].append(2)

# Print the dictionary
print(dictionary)