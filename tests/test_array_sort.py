import  unittest
from Python_Practices import arraysort

class TestArraySort(unittest.TestCase):
    def test_array_sort(self):
        arraysort.array_sorting([1, 2, 3, 4, 5])

    def test_that_array_sort(self):
        actual = arraysort.array_sorting([1, 2, 3, 4, 5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(actual, expected)
