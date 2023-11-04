# The _sre module provides functions for working with regular expressions.

import _sre

regex = _sre.compile("Hello, world!")

match = regex.search("Hello, world!")

if match:
    print("Match found!")
else:
    print("Match not found!")