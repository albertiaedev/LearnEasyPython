# The _ast module provides classes for representing the abstract syntax tree (AST) of Python code.

import _ast

tree = _ast.parse("print('Hello, world!')")

print(tree)