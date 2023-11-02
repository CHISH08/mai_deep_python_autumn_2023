import unittest
from main2 import Data

import unittest

class TestDataDescriptors(unittest.TestCase):
    def test_integer_value(self):
        with self.assertRaises(ValueError):
            data = Data('string', 'data', 100)  # Передаем строку вместо целого числа

    def test_string_value(self):
        with self.assertRaises(ValueError):
            data = Data(10, 42, 100)  # Передаем число вместо строки

    def test_positive_integer_value(self):
        with self.assertRaises(ValueError):
            data = Data(10, 'data', -2000)  # Передаем отрицательное число вместо положительного целого числа

    def test_norm_attributes(self):
        data = Data(10, 'data', 2000)
        self.assertEqual(data.num, 10)
        self.assertEqual(data.name, 'data')
        self.assertEqual(data.price, 2000)

if __name__ == '__main__':
    unittest.main()
