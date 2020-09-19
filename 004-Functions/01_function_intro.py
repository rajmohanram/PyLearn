"""
Functions:
    - Allows reuse of code
    - To create modular program
    - DRY - Don't Repeat Yourselves
"""


# def: keyword to define a function
# hello_func(): name of the function - Prints a string when called
# () - used to get the parameters: No parameters / arguments used in this function
def hello_func():
    print("Hello World!, Welcome to Python function")


# hello_func_return(): name of the function - Returns a string when called
def hello_func_return():
    welcome = "Hello World! Welcome to PYTHON FUNCTION"
    return welcome


# main program
if __name__ == "__main__":
    # call the function by its name
    hello_func()

    # get a value returned from a function & print it
    greeting = hello_func_return()
    print(greeting)
