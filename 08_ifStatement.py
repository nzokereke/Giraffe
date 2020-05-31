"""  ------------ control flow: ------------
     control flow tools control the flow of the program
     'if', 'while' and 'for' are used for this purpose.
     Control flow tools (if for and while) require

     ---------   condition statement   -----------
     control flows involve the evaluation of a condition statement
     this is usually seen in the form of comparing two variables
     using operators
     == equals
     >  greater
     <  less than
     != not equal to
     >= greater or equal to
     --- logical operators -----
     used when comparing multiple conditions:
     and  - if all the conditions are met
     or   -  at least one condition is met
     not  -  condition is not met or false

     ------------------------ if & elif -------------------------
     if  - this control flow is used when a certain condition is met then an action is triggered
     elif (else if) - if the first condition is not met then elif checks for the 2nd condition and triggers
          another action.

     - example using 'if' and 'elif' and operators: '=' , '<', and '>'    """
x = 8
number = int(input('enter a number: '))
if number == x:
    print('you have guessed correctly')
elif number > x:
    print('go lower')
elif number < x:
    print('go higher')

'''    ---- example using 'if' and the logical 'and' operators  ---------------'''
age = int(input(' enter age: '))

if age > 17 and age < 60:  # can be simplified to  -  17 < age < 60
    print('you are not entitled to a free bus pass')
else:
    print('you are not entitled to a free bus pass')

'''    ---- example using 'if' and the logical 'or' operators  ---------------'''

a = 1
b = 2
c = 3

choice = int(input(' make a selection: (1) crispy korean chicken, (2) chili chicken (3) kebab: '))
if choice == a or choice == b:
    print(' yum yum')
elif choice == c:
    print('no thanks, lost my appetite ')
else:
    print('not a valid selection')