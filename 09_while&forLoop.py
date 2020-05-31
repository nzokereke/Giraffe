""" ---------  Condition Statement: While Loop  ---------------
   1. Here you iterate a statement as long as the condition is true
   2. usually when the number of times to iterate is unknown
   2. A variable is declared where that condition is tested (counter)
"""

# x = 0
#
# while x < 5:
#     print('loop,', x)
#     x += 1

''' -----------------  for loop ------------------------------------'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even = []
odd = []
for a in numbers:
    if a % 2 == 1:
        odd.append(a)
    elif a % 2 == 0 and a != 0:
        even.append(a)

print('new list of even numbers', even)
print('new list of odd numbers', odd)
