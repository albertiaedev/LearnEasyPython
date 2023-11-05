# The _token module provides functions for tokenizing Python code.

import _token

tokens = _token.tokenize("print('Hello, world!')")

for token in tokens:
    print(token)