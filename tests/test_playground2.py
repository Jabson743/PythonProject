import unittest
from Python_Practices import playground2

class TestPlayground2(unittest.TestCase):
    def test_playground2(self):
        playground2.swap_character('abc', 'xyz')

    def test_that_character_can_be_swapped(self):
        actual = playground2.swap_character('abc', 'xyz')
        expected = 'xyc abz'
        self.assertEqual(actual, expected)
