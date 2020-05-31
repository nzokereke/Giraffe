"""
    Except, Try  is the way python deals with exception handling
    try - lets you test for errors, stops the program from crashing
    except - handles the error
    Python has built in Exception functions couple of examples
    1. errno: A numeric error code from the C variable errno.
    2. NameError: Raised when a local or global name is not found. This applies
    only to unqualified names. The associated value is an error message that
    includes the name that could not be found.
    3. IndexError: Raised when a sequence subscript is out of range. (Slice
    indices are silently truncated to fall in the allowed range; if an index
    is not an integer, TypeError is raised.)
    go to python.org to view more (https://docs.python.org/3/library/exceptions.html#Exception)
"""

# example 1

try:
    print(name)  # variable name has not been declared
except:
    print('an error has occurred')

# example 2  - many exceptions
check = 1
try:
    print(check + 'two')
except NameError:  # built-in exception
    print('variable not defined')
except:
    print('error detected')

# example 3 - using built in exception
# 0/0 will generate an error
a = 0
b = 0

try:
    c = a / b
    print(c)
except ArithmeticError:
    print('arithmetic error')
finally:   # this is executed whether or not an error occurs
    print('finished')
