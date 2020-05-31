"""
dictionary is a collection of unordered, changeable, indexed and related data pairs
enclosed in  curly brackets and declared using key and values also
referred to as key - value pairs.
To declare a dictionary the syntax is {key : data}
multiple pairs are separated by commas ',' {key : data, key : data, key : data}
* Note keys must be unique
"""

student_1 = {'name': 'joanna', 'stream': 'data', 'modules_completed': 4, 'location': '125 LW'}

print(student_1)
print(student_1['stream'])

# you do not have to assign a value when declaring a dictionary'''
empty = {}

''' 
you can also declare a dictionary using the 'dict' method. when  you use this method you use 
parentheses () instead of curly brackets {} 
'''
football = dict(league='premier', team='arsenal', stadium='emirates', location='Highbury')

''' to access a value '''
print(football['league'])

''' to modify a value in a dict '''
football['location'] = 'islington'
print(football['location'])

''' to remove a key:value'''
del football['location']
print(football)

''' to add a new key value pair '''
football['location'] = 'Highbury'
print(football)
