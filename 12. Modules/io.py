# The _io module provides classes and functions for working with streams of data.

import _io

f = _io.StringIO()

f.write("Hello, world!")

print(f.getvalue())