# The _warnings module provides functions for issuing warnings.

import _warnings

_warnings.warn("This is a warning!")

try:
    # Do something that might raise a warning
    pass
except Warning as e:
    print(e)