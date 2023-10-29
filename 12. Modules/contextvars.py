# The _contextvars module provides classes and functions for managing context variables.

import _contextvars

context = _contextvars.Context()

context.set("name", "Alice")

def hello():
    print(f"Hello, {context.get('name')}!")

hello()