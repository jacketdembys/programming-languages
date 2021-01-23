

# function to print a separating line
def print_separate_line(count, motif="*"):
    print("\n")
    if motif == "*":
        for i in range(count):
            print("*", end=" ")
        print("\n")