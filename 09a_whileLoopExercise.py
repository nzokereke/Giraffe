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