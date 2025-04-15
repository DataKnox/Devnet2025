import unittest
from main import calculate_rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_rectangle_area(5, 4), 20)
        self.assertEqual(calculate_rectangle_area(2.5, 3.5), 8.75)
        
    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(0, 5)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, 0)
            
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 4)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, -4)

if __name__ == '__main__':
    unittest.main() 