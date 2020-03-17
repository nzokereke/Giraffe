# a = True
# # y = False
# # print(bool(a == y))
# # print(a == y)
# # print(bool(a != y))
# # print(a != y)
# # print(bool(a >= True))
# # print(a >= True)
# # print(bool(y <= False))
# # print(y <= False)
# floatnum = 1.5
# intnum = 7
# half = 1/2
# print(floatnum + intnum + half)
# print(intnum/floatnum)
# print(floatnum * intnum)

# escape_example_1 = 'I said \'Wow!\''
# # Quote_in_quote = 'I said "Wow!"'
# # Reverse_quote_in_quote = "I said 'wow!'"
# # print(escape_example_1)
# # print(Quote_in_quote)
# # print(Reverse_quote_in_quote)

# Hw = "Hello! World"
# print(Hw[7:])
# print(Hw[-5:])
# print(Hw[0:5])
# print(Hw[:5])
#
# # Length of Strings
# print(len(Hw))

# z = 10
# o = 85
# c = 10
## print(z == o)
# print(z != o)
# print( z != c)

# mixture = [1, 2, 3, "one", "two", "three", "delete_me"]

# print(mixture[1:3])
# print(mixture[-2::])
# print(mixture[::2])
# print(mixture[0:3])
# print(mixture[1:3])
# print(mixture[2:3])
# print(mixture[3:3])
# print(mixture[-0::])
# print(mixture[-1::])
# print(mixture)
# print(mixture[2:7])
# print(mixture[0:4])
# # del mixture[-1]
# # print (mixture.append("added"))
# print(mixture)
# import pprint
# #
# #
# # student_1 = {
# #     "name": "susan",
# #     "stream": "tech",
# #     "completed_lessons": 4,
# #     "completed_lesson_names": ["variables", "data_types", "set up"]
# # }
# # pprint.pprint(dict(student_1, indent=1))
# # print(student_1["stream"])
# # print(student_1["completed_lesson_names"][0])

# film_rating = "12a"
#
# if film_rating.lower() == "universal":
#     print("all age groups can watch this film")
# elif film_rating.lower() == "pg":
#     print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating.lower() == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable "
#           "for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating.lower() == "15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
#     print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#     print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

# in the example below if you change the elif to if it will return
# two out puts rather than one
# def analyzeAge(age):
#     if age < 21:
#         print("You are a child")
#     elif age >= 21:  # Greater than or equal to
#         print("You are an adult")
#     else:  # Handle all cases where 'age' is negative
#         print("The age must be a positive integer!")
#
#
# analyzeAge(18)

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# embedded_lists2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
#              3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2)

# for data in embedded_lists2:
#     print(data)
#     for num in list_data:
#         print(num)

# d_data = {1: {'name': 'adam bradley', 'stream': 'Eng', 'class': 'Eng60', 'location': '125lw'},
#           2: {'name': 'charlie moore', " stream": 'Eng', 'class': 'Eng60', 'location': '125lw'},
#           3: {'name': 'brandon connelly', 'stream': 'SDET', 'class': 'Eng61', 'location': 'birmingham'},
#           4: {'name': 'franca duru', 'stream': 'Eng', 'class': 'Eng60', 'location': '125lw'},
#           5: {'name': 'Phoebe keke', 'stream': 'ba', 'class': 'ba45', 'location': '125lw'}
#           }

# for items in d_data.values():
#     if items['name'] == 'adam bradley':
#         print('I have found "adam"')
# ---------------------------------
# else:
#    print(items['name'])
# ----------------------------------------

# x = 0
# while x <= 5:
#     print('we have gone round the loop {} times'.format(x))
#     x = x + 1 #incrementor
#     if x == 4:
#         break

# def print_something():
#     print('print_string')
#
#
# print_something()


# def name(arg1 = 'ngozi', arg2= 'Keke'):
#     return str(arg1 + arg2)
#
#
# print(name())
# def add(num1, num2):
#     return num1 + num2


# addition = lambda num1, num2: num1 + num2
#
# print(add(2, 2))
# print(addition(2, 2))

# savings = [234.00, 555.00, 674.00, 78.00]
#
# bonus = list(map(lambda x: x * 1.1, savings))
#
# bonus_2 = lambda x: x * savings
#
# print(bonus)
# print(bonus_2(int(1.1)))

