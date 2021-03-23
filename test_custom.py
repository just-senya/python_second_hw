import unittest
from custom import CustomList

class CustomTest(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList([4, 4, 4, 4])

    def test___add__(self):
        adder1 = CustomList([1, 2, 3, 4])
        adder2 = [1, 2, 3, 4]
#        adder3 = [1, 2, 3, '4']
        
        self.assertEqual(self.custom_list + adder1, CustomList([5, 6, 7, 8])) 
        self.assertEqual(self.custom_list + adder2, CustomList([5, 6, 7, 8])) 
#        self.assertRaises(self.custom_list + adder3, TypeError) 

    def test___sub__(self):
        subtrac1 = CustomList([1, 2, 3, 4])
        subtrac2 = [1, 2, 3, 4]

        self.assertEqual(self.custom_list - subtrac1, CustomList([3, 2, 1, 0]))
        self.assertEqual(self.custom_list - subtrac2, CustomList([3, 2, 1, 0]))

    def test___lt__(self):
        self.assertTrue(self.custom_list < CustomList([5, 5, 5, 5]))
        self.assertFalse(self.custom_list < CustomList([3, 3]))

    def test___gt__(self):
        self.assertTrue(self.custom_list > CustomList([3, 3]))
        self.assertFalse(self.custom_list > CustomList([5, 5, 5, 5]))

    def test___le__(self):
        self.assertTrue(self.custom_list <= CustomList([4, 4, 4, 5]))
        self.assertTrue(self.custom_list <= CustomList([4, 4, 4, 4]))
        self.assertFalse(self.custom_list <= CustomList([3, 3]))

    def test___ge__(self):
        self.assertTrue(self.custom_list >= CustomList([4, 4]))
        self.assertTrue(self.custom_list >= CustomList([4, 4, 4, 4]))
        self.assertFalse(self.custom_list >= CustomList([5, 5, 5, 5]))

    def test___ne__(self):
        self.assertTrue(self.custom_list != CustomList([4, 4]))
        self.assertFalse(self.custom_list != CustomList([4, 4, 4, 4]))

    def test__eq__(self):
        self.assertTrue(self.custom_list == CustomList([4, 4, 4, 4]))
        self.assertFalse(self.custom_list == CustomList([4, 4]))
