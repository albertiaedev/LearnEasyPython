# The _weakref module provides classes and functions for creating weak references.

import _weakref

class MyClass:
    pass

obj = MyClass()

weakref = _weakref.ref(obj)

print(weakref())

del obj

print(weakref())