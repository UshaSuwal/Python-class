from day18 import test1
def product(a,b):
    return a*b
print(product(2,4))

# even if test1 is imported, it wont be run in this test2 module
# Note: number bata start vako module lai import garna mildaina because it is identifier


## Import way:

# if built-in:
import csv
import json
# import pandas as pd  pandas lai pd naming diyeko

from day18.test1 import num