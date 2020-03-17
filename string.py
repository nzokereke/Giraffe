# prints a string within the open and closed brackets
print("Elephant Academy")

# '\n' moves the proceeding string to the next line
print("Elephant\nAcademy")

# '\"' tells python to treat " as a string
print("Elephant\" Academy")

# define a variable
phrase = "Elephant Academy"

# print variable
print(phrase)
phrase = "Elephant Academy"

# concatenate a variable and string
print(type(phrase + " is cool"))

# string functions
print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.upper().isupper())

# returns the length of a string
print(len(phrase))
# returns the character in a given position e.g. [1], [2]
print(phrase[0])

# returns the position of a character
print(phrase.index("p"))
print(phrase.index("ant"))

# replaces a string with another
print(phrase.replace("Elephant", "Giraffe"))
print(phrase.isalnum())
num = 5

print(phrase + num)
print(phrase, num)
print(float(num))
print(type(float(num)))
# slicing
print(phrase[:3])
print(phrase[0:5])
print(str.strip(phrase))
print(len(phrase))

