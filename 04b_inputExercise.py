""" calculate how many pizza slices are needed to satisfy your hungry friends
1. medium pizza consists of 6 slices
2. large pizza 8 slices
"""

friends = input('enter no. of friends: ')
slices_of_pizza = 3
total_slices = int(slices_of_pizza) * int(friends)
medium_sized_pizza = int(slices_of_pizza) * int(friends)/6
print('you will need {} slices of pizza or {} medium sized pizza'.format(total_slices,medium_sized_pizza ))