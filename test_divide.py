# Test file for divide.py
import unittest
from divide import divide

class TestDivide(unittest.TestCase):
    
    def test_divide(self):
        self.assertEqual(divide(4,2), 2, "Should be 2")
        self.assertEqual(divide(0,5), 0, "Should be 0")
        self.assertEqual(divide(-10,2), -5, "Should be -5")
        self.assertRaises(ZeroDivisionError, divide, 1, 0)

if __name__ == '__main__':
    unittest.main()
