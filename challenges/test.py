# list comprehension with python

# traditional for-loop
def list_doubler_0(lst):
    doubled = []
    for num in lst:
        doubled.append(num*2)
    return doubled

# list comprehension function
# ["operation to perform in the loop" for "iterator" in "iterable list"]
# "operation to perform in the loop" return a result that gets added to the list
def list_doubler_1(lst):    
    doubled = [(num*2) for num in lst]
    return doubled  

# returning the list comprehension directly is also possible
def list_doubler_2(lst):    
    return [(num*2) for num in lst]

# list comprehension can also be used with conditional statement
# Let us recall the use of a conditional stratement in a traditional for-loop
def long_words_finder_0(lst):
    words = []
    for word in lst:
        if len(word) > 5:
            words.append(word)
    return words       

# now let us apply the list comprehension learned before
def long_words_finder_1(lst):
    return [word for word in lst if (len(word)>5)]


# main function where the functions are being tested:
if __name__ == '__main__':

    # inline for loop tutorial
    my_list = [21,2,93]

    my_doubled_list_0 = list_doubler_0(my_list)
    my_doubled_list_1 = list_doubler_1(my_list)
    my_doubled_list_2 = list_doubler_2(my_list)

    words = ['blog', 'Treehouse', 'Python', 'hi']
    long_words_0 = long_words_finder_0(words)
    long_words_1 = long_words_finder_1(words)

    print("original:", my_list)
    print("doubled 0:", my_doubled_list_0)
    print("doubled 1:", my_doubled_list_1)
    print("doubled 2:", my_doubled_list_2)
    print("\n")
    print("original:", words)
    print("long words 0:", long_words_0)
    print("long words 1:", long_words_1)