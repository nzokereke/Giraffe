import unittest

from items_function import password


class TestPassword(unittest.TestCase):
    def test_password_short(self):
        result = password.password_short('Password2020')
        self.assertTrue(result)

    def test_password_long(self):
        result = password.password_long('Password2020')
        self.assertTrue(result)

    def test_password_upper(self):
        result = password.password_has_uppercase('Password2020')
        self.assertTrue(result)

    def test_password_lower(self):
        result = password.password_has_lowercase('Password2020')
        self.assertTrue(result)

    def test_password_digit(self):
        result = password.password_has_digits('Password2020')
        self.assertTrue(result)

    def test_password_space(self):
        result = password.password_has_blank_space('Password2020')
        self.assertTrue(result)

    def test_password_special_xter(self):
        result = password.password_has_special_xters('Password2020')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
