# The _importlib module provides classes and functions for importing Python modules.

import _importlib

# Import a module
module = _importlib.import_module("math")

# Call a function from the module
print(module.pi)