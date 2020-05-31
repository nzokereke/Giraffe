""" this class Password comes with a method that checks if a password
    1. greater than 8 characters
    2. less than 8
    3. has at least one capital character
    4. has a least one lower case character
    5. has at least one digit
    6. no white space / space  in password

"""


class Password:

    def check_password(self, password):

        if len(password) < 8:
            return False
        if len(password) > 12:
            return False
        if not any(x.isupper() for x in password):
            return False
        if not any(x.islower() for x in password):
            return False
        if not any(x.isdigit() for x in password):
            return False
        if ' ' in password:
            return False
        else:
            return True

