# The _opcode module provides classes and functions for working with Python bytecode.

import _opcode

opcode = _opcode.opmap["LOAD_CONSTANT"]

print(opcode)