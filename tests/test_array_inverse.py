import unittest
from Python_Practices import inversearray

class TestArrayInverse(unittest.TestCase):
    def test_array_inverse(self):
        inversearray.array_inverse([1, 2, 3, 4, 5])

    def test_array_that_can_inverse(self):
        actual = inversearray.array_inverse([1, 2, 3, 4, 5])
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)
