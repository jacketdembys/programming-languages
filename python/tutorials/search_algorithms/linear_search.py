"""
Implementations of linear search in Python
Author: Jacket Demby's / University of Missouri-Columbia
"""

import numpy as np


search_array = [10,14,19,26,27,31,33,35,42,44]
search_number = 33


print()
print("Linear search in progress ...")
print("Search item is:", search_number)
print()

for item in search_array:
    if item == search_number:
        print("search item", item,"found at index", search_array.index(item))