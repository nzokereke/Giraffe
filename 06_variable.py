""" variables are names given to data that we need to store and manipulate in
 a program. A variable is assigned a value
 """
# define a variable 'phase is the variable' and the string 'Elephant Academy' is stored in the variable
phrase = "Elephant Academy"
integer = 100
decimal = 7.5
text = 'hello'

# naming convention - camel case or underscores
checkForNumber = 1
check_for_number = 2

# print variable
print(phrase)
phrase = "Elephant Academy"

# you can define multiple variables at one go
age, name = 35, 'Phoebe'
print(name, age)

# naming a variable  - you can use alpha and numeric characters. However your variable name cannot start with a number.
# variables are also case sensitive.
# 1change = 5 # this comes up as an error
change1 = 10

# concatenate a variable and string
print(type(phrase + " is cool"))