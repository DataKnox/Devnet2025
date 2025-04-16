import unittest
from math_operations import divide

class TestMathOperations(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(100, 4), 25.0)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)

    def test_divide_decimal_numbers(self):
        self.assertEqual(divide(1.5, 0.5), 3.0)
        self.assertEqual(divide(0.1, 0.01), 10.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main() 