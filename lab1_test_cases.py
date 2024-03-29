import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
	#Test a few simple cases along with edge cases.
	#Empty list, None Type, first element is right, last is right

        tlist = None

        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([5, 3, 4, 1]), 5)
        self.assertEqual(max_list_iter([5, 5, 5, 5]), 5)
        self.assertEqual(max_list_iter([4, 6, 7, 9]), 9)


    def test_reverse_rec(self):
        # Test None type list
        tlist= None

        with self.assertRaises(ValueError):
            reverse_rec(tlist)

        # Test common and edge cases of empty list and list of one element.
        # Test cases with weird symmetry (5, 5, 5)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([5, 5, 5]), [5, 5, 5])


    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        # Test None Type list
        tlist = None

        with self.assertRaises(ValueError):
            bin_search(0, low, high, tlist)

        # Test empty list,searching left, searching right, not finding anything

        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
        self.assertEqual(bin_search(0, 1, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 6)
        self.assertEqual(bin_search(0, 1, 10, []), None)
if __name__ == "__main__":
        unittest.main()

    
