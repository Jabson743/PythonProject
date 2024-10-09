from Python_Practices import validemail
import unittest

class TestValidemail(unittest.TestCase):
    def test_validemail(self):
        validemail.email_validation("Iyanda43@gmail.com")

    def test_that_email_is_valid(self):
            actual = validemail.email_validation("Iyanda43@gmail.com")
            expected = True
            self.assertEqual(actual, expected)

    def test_that_email_is_not_valid(self):
            actual = validemail.email_validation("Iyanda4@gmail.com")
            expected = False
            self.assertEqual(actual, expected)