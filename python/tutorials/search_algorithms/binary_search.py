"""
Implementations of binary search in Python
Author: Jacket Demby's / University of Missouri-Columbia
Date: 01/22/2021
"""
# data should be in the sorted form

from search_functions import *

# function for linear search
def binary_search(search_array, search_number):

    print()
    print("Binary search in progress ...")
    print("Input array is:", search_array)
    print("Search item is:", search_number)
    print()
    print_separate_line(50)
    comparisons = 0

    # sort the array
    search_array_sorted = sorted(search_array)
    num_elements = len(search_array_sorted)
    lower_bound = 1
    upper_bound = num_elements

    #print("Sorted input array is:", search_array_sorted)

    if upper_bound < lower_bound or search_number not in search_array_sorted:
        print("Search item does not exist in search array")

    for i in range(num_elements):
        comparisons += 1

        #mid_point = round(lower_bound + (upper_bound - lower_bound)/2)
        mid_point = int(lower_bound + (upper_bound - lower_bound)/2)
        #print("mid_point", i, mid_point)
        #print("Sorted input array is:", search_array_sorted)

        if search_array_sorted[mid_point] < search_number:
            lower_bound = mid_point + 1
        if search_array_sorted[mid_point] > search_number:
            upper_bound = mid_point - 1
        if search_array_sorted[mid_point] == search_number:
            print("search item", search_array_sorted[mid_point],"found at index", search_array.index(search_array_sorted[mid_point]))
            print("Number of comparisons made:", comparisons)
            break
        

# main function
if __name__ == "__main__":
    search_array = [10,33,14,35,42,19,26,44,27,31]
    search_number = 31
    binary_search(search_array, search_number)