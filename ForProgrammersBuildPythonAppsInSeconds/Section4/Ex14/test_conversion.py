import unittest
from height import convert

class ConversionTestCase(unittest.TestCase):
    def test_conversion(self):
        feet_inches = "5 6"  # Sample input
        result = convert(feet_inches)
        
        self.assertIsInstance(result, float)  # Check if the result is of type float
        self.assertGreaterEqual(result, 0)  # Check if the result is non-negative

if __name__ == '__main__':
    unittest.main()