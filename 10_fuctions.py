"""
functions : code that performs a specific task
1. to create your function you start with  the keyword 'def' and assign it with something descriptive  - 'say Hi'.
2. end it with open and closed brackets and colon; this indicates to python that anything following this, is code
   relating to the function, the closed brackets can contain parameter(s).
   * Note a parameter is similar to a variable the only difference is its usage (enclosed within parentheses)
3. A function can be reused throughout the program
"""


# below is a simple function with one line of code

def say_hi():
    print("Hello User")


# to run the code in the function you need to call it
say_hi()


# This example contains a parameter 'name' when calling the function you will assign a value to the parameter

def greeting(name):
    print("Hello " + name)


greeting("Zoe")  # this will print Hello Zoe
greeting("Phoebe")


# you can use more than one parameter to define a function
def user_info(name, age):
    print("Hello " + name + " you are " + age + " years old")


user_info("Phoebe", "39")

# here is a function that uses the for loop and an if statement
# this function checks if a number is an even or odd number using the modulus
check = [57, 83, 117, 61, 731, 953, 112, 1, 4, 5, ]


def prime(int1):
    even = []
    odd = []
    for x in int1:
        if x % 2 == 0:
            even.append(x)
        elif x % 2 > 0:
            odd.append(x)
    print('even numbers', even)
    print('even numbers', odd)


prime(check)

'''
   ************************ variable scope ********************
   variables defined within a function are treated differently to variable defined outside a function
1. a variable defined within a function is only accessible within that function and cannot be
   'called' out side that function. this type of variable is called a *local variable*.
2. Any variable declared outside a function is referred to as a global variable and can be called
   by a function i.e accessible anywhere in the program.

'''

'''
   ********************** Default Parameters ***********************
1. You can define default values  for parameters
2. If a parameter has a default value we do not have to pass a value
   for that parameter when calling a function
3. * Note all parameters with default values must be placed last in the parameter list
'''


# example of a function using default values
def default_value(a=1, b=2, c=3):
    print(a, b, c)


default_value()

'''
    ********* Variable Parameter Length **********
    1. you can pass a variable number of parameters
    2. use * to indicate a variable parameter length
'''


# example of function using a variable parameter length
def variable_num(*a):
    total = 0
    for y in a:
        total += y
    print(total)


variable_num(1, 2, 3, 4, 5)  # non key-worded variable length arg. list


# example of key-word variable length


def v_key(**b):
    for x, y in b.items():  # items_function is a dictionary function
        print("id = %s, name = %s" % (x, y))


v_key(id1="john", id2='jack')
v_key(id3="johnson", id4='jason', id5="justin", id6='jerry')

''' ********** Importing Modules **********
   1. python has a number of built in functions 
   2. these kind of functions are saved in a file called items_function 
   3. to use these functions you need to import them  
   4. to import a built in function you use the keyword 'import'
   
'''

# to import an entire module
import random

# to import a function within the module
from random import randrange
