"""  -------     Exercise ----------------
write a program to check  that Only Individuals who
1. live in London and  are
2. 60 years or over
3. under the age of 18
are eligible  for a free buss pass """

a = input("enter age: ")
b = input("enter city of residence: ")
if a < '18' or a > '59' and b == 'london':
    print("you are eligible for a free bus pass ")
elif a < '18' or a > '59' and b != 'london':
    print("you do not reside in london so not eligible for a free bus pass")
else:
    print("you do not meet the criteria for a free london bus pass")

''' ---------- Exercise ----------------------
A guessing game exercise - Guess the number
1. user enters a number 
2. number is compared to declared variable 
3. depending on the number a msg should be displayed requesting that the user go higher or lower  '''

running = True
number = 18
while running:
    guess = int(input('\nenter a number: '))
    if guess == number:
        print('well done you have guessed correctly', end='')
        exit()
    elif guess > number:
        print('not correct go lower'.title(), end='')
    else:
        print('not correct go higher', end='')
print('\ndone')
exit()

