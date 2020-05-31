"""
create a program where the user inputs 2 integers and divides one input by the other
display specific error messages when running your program
  1. when user does not enter a number
  2. when the user tries to divide 0 by 0
  3. any other input error
"""
try:
    int1 = int(input('Enter a number: '))
    int2 = int(input('Enter a number: '))
    result = int1 / int2
    print('your answer is: ', result)
except ValueError:
    print('Error: You did not enter an integer')
except ArithmeticError:
    print('Error: Cannot divide an integer by 0')
except Exception as e:
    print('Unknown error: ', e)
finally:
    print('finished')
