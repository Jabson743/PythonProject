import unittest
from Python_Practices import playground3

class TestPlayground3(unittest.TestCase):
    def test_playground3(self):
        playground3.divided_equally("he.ll,o")

    def test_that_the_middle_can_be_divided_equally_add(self):
        actual = playground3.divided_equally("he,ll.o")
        expected = "hello"
        self.assertEqual(actual, expected)