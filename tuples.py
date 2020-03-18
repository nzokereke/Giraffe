# tuples a type of data structure or collection, a container
# where we can store different values
# tuples once created cannot be changed
#  tuples are enclosed in ( ) brackets

# here is how you create a tuple with integers
coordinates = (4, 5)
print(coordinates[0])

# empty tuple
empty = ()
print(empty)

# tuple with different data types
mixer = (18, 'March', 2020, 1.1)
print(mixer)

# nested tuple
nest = ('Location', [9, 17, 31], (41.24, 2028.2, 10.4418), 'coordinates')
print(nest)

# a tuple with 1 element must always have a trailing comma
one_element = ('Hello World',)
string_element = ('Hi World')  # parentheses are redundant here just highlighting difference
print(type(one_element))
print(type(string_element))

" a tuple can be created without using parentheses"
missing = 'lost', 'found', 11.03, 20
print(missing)
print(type(missing))