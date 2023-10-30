# The _csv module provides classes and functions for reading and writing CSV files.

import _csv

with open("data.csv", "r") as f:
    reader = _csv.reader(f)

    for row in reader:
        print(row)