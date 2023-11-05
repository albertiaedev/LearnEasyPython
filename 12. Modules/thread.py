# The _thread module provides functions for implementing multithreading in Python.

import _thread

def worker():
    print("Worker thread running!")

_thread.start_new_thread(worker, ())

while True:
    pass