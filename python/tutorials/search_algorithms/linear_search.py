"""
Implementations of linear search in Python
Author: Jacket Demby's / University of Missouri-Columbia
Date: 01/22/2021
"""

# function for linear search
def linear_search(search_array, search_number):

    print()
    print("Linear search in progress ...")
    print("Input array is:", search_array)
    print("Search item is:", search_number)
    print()
    print_separate_line(50)
    comparisons = 0
    
    for item in search_array:
        comparisons += 1
        if item == search_number:
            print("search item", item,"found at index", search_array.index(item))
            print("Number of comparisons made:", comparisons)

# function to print a separating line
def print_separate_line(count, motif="*"):
    if motif == "*":
        for i in range(count):
            print("*", end=" ")
        print("\n")


# main function
if __name__ == "__main__":
    search_array = [10,14,19,26,27,31,33,35,42,44]
    search_number = 33
    linear_search(search_array, search_number)
