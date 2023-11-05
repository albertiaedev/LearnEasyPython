# The _threading module provides classes and functions for implementing multithreading in Python.

import _threading

class Worker(threading.Thread):
    def run(self):
        print("Worker thread running!")

worker = Worker()
worker.start()

worker.join()