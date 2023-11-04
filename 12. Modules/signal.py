# The _signal module provides functions for handling signals.

import _signal

def handler(signal, frame):
    print("Signal received!")

_signal.signal(_signal.SIGINT, handler)

while True:
    pass