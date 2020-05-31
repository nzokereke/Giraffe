""" tuples are lists but you cannot modify their values (immutable)
    a good example is a list of months - this will obviously never change,
    tuples are enclosed in parentheses()
    similar to lists you can access a value of a tuple using their index
    Note even though a tuple is declared using ()"""
months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
''' months[7] = aug
    months[-1] = dec'''
print(months[7])
print(months[-1])
