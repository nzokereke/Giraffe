# # collections categorised into 4 different types
# 1. lists,
# 2. Dictionaries
# 3. tuples
# 4. Sets and frozen sets
#
# #  ***********  list functions ***************
# countries = ["Nigeria", "Ghana", "Senegal",
#              "Liberia", "Gambia", "Tanzania"]
# print(countries)
# print(countries[0])
# print(countries[-2])
# print(countries.count("Tanzania"))
#
''' append attaches a new element to an exiting list'''
# countries.append("Algeria")
# print(countries)
#
# # insert a new element to the list in a specific position
# countries.insert(3, "Botswana")
# print(countries)
#
''' extend adds lists together'''
# lucky_numbers = [6, 10, 15, 20, 49, 80, 232]
# countries.extend(lucky_numbers)
# print(countries)
#
''' remove an element from a list'''
# countries.remove("Liberia")
# print(countries)
#
''' clear all elements from a list '''
# countries.clear()
# print(countries)
#
''' pop - removes the last element from a list'''
# countries = ["Nigeria", "Ghana", "Senegal", "Gambia", "Tanzania", "Algeria", "Senegal", "Liberia"]
# print(countries)
# countries.pop()
# print(countries)
#
''' index can be used to find an element in a list '''
# print(countries.index("Ghana"))
#
# # count how many elements are in a list
# print(countries.count("Senegal"))
#
''' sort the list in ascending order'''
# countries.sort()
# print(countries)
#
'''reverse the order'''
# countries.reverse()
# print(countries)
#
'''copy'''
# countries2 = countries.copy()
# print(countries2)
#
# print(countries.count("Senegal"))

''' *********** Exercise *****************
# Create a list with odd and even numbers
# sort the list into 2 new list, 1 with even numbers 
# and the other # with odd numbers 
# ***************************************** '''
odd_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
odd_list = []
even_list = []
for x in odd_even:
    if (x % 2) > 0:
        odd_list.append(x)
    else:
        even_list.append(x)
print(odd_list)
print(even_list)
