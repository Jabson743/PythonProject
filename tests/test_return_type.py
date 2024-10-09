import unittest
from Python_Practices import returntype

class TestReturnType(unittest.TestCase):
    def test_return_type(self):
        returntype.return_type("Girl")

    def test_that_letters_can_be_count(self):
        actual = returntype.return_type("awe")
        expected = {"a": 1, "w": 1, "e": 1}
        self.assertEqual(actual, expected)

    def test_that_letters_can_exists_twice(self):
        actual = returntype.return_type("Football")
        expected = {"F": 1, "o": 2, "t": 1, "a": 1, "b": 1, "l": 2}
        self.assertEqual(actual, expected)

    def test_that_letters_can_hold_multiple_values(self):
        actual = returntype.return_type("Bloom")
        expected = {"B": 1, "l": 1, "o": 2, "m": 1}
        self.assertEqual(actual, expected)

