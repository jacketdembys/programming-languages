# import the necessary libraries
import argparse

"""
    argparse supports positional arguments and optional arguments
    the positional arguments are mandatory and cannot be skipped otherwise an error occurs
"""


if __name__ == "__main__":

    # intialize the object of the class
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")

    # get the values of the commands the user has passed 
    args = parser.parse_args()

    # print the values entered
    print("first number is: ", args.number1)
    print("second number is: ", args.number2)
    print("operation is: ", args.operation)

    # perform the desired operation
    # whenever you pass an information to the parser, it comes by default as a string
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "substract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2
    elif args.operation == "divide":
        result = n1 / n2
    else:
        print("Unsupported operation")

    # return the result
    print("\nThe result is :", result)
