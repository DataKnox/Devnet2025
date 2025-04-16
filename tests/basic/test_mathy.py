import unittest
from mathy import add_numbers

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 4), 7, "Should be 7 when adding 3 and 4")

if __name__ == "__main__":
    unittest.main()