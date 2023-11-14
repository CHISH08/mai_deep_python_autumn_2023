import unittest
from unittest.mock import patch
import main


class TestCustomListOperations(unittest.TestCase):
    def setUp(self):
        self.lst1 = main.lst1
        self.lst2 = main.lst2

    def test_addition(self):
        result = self.lst1 + self.lst2
        self.assertEqual(result, main.CustomList([6, 6, 9, 4, 5]))
        result = self.lst1 + [10, 3, 4, 1]
        self.assertEqual(result, main.CustomList([11, 5, 7, 5, 5]))
        result = [10, 3, 4, 1] + self.lst1
        self.assertEqual(result, main.CustomList([11, 5, 7, 5, 5]))

    def test_subtraction(self):
        result = self.lst1 - self.lst2
        self.assertEqual(result, main.CustomList([-4, -2, -3, 4, 5]))
        result = self.lst2 - self.lst1
        self.assertEqual(result, main.CustomList([4, 2, 3, -4, -5]))

    def test_comparison(self):
        self.assertFalse(self.lst1 < self.lst2)
        self.assertTrue(self.lst1 <= self.lst2)
        self.assertTrue(self.lst1 == self.lst2)
        self.assertFalse(self.lst1 != self.lst2)
        self.assertFalse(self.lst1 > self.lst2)
        self.assertTrue(self.lst1 >= self.lst2)
        print(self.lst1, self.lst2, sep="\n")


if __name__ == "__main__":
    unittest.main()
