"""
Implementations of hash tables in Python
Author: Jacket Demby's / University of Missouri-Columbia
Date: 01/22/2021
"""
from search_functions import *

# hash tables are implemented in Python in the dictionary datastructure
# So we see the implementation of hash table by using the dictionary data 
# types as below.

# declare a dictionary
dict_test = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First'
}

# accessing the dictionary with its key
print()
print("dict_test['Name']:", dict_test['Name'])
print("dict_test['Age']:", dict_test['Age'])
print("dict_test['Class']:", dict_test['Class'])

# updating a dictionary
dict_test['Age'] = 8
dict_test['School'] = 'CEPE Selima'   # add a new entry

print_separate_line(50)

print("dict_test['Name']:", dict_test['Name'])
print("dict_test['Age']:", dict_test['Age'])
print("dict_test['Class']:", dict_test['Class'])
print("dict_test['School']:", dict_test['School'])

# delete a dictionary entry
print_separate_line(50)
del dict_test['Name']       # remove entry with key 'Name'
print(dict_test)

dict_test.clear()                # remove all entries
print(dict_test)

"""
del dict_test               # delete entire dictionary
print(dict_test)
"""