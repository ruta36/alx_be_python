import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10.5, 2.2), 12.7)  # Test with floats

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, -2), 12)
        self.assertEqual(self.calc.subtract(3.14, 1.5), 1.64)  # Test with floats

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(2.5, 2), 5)  # Test with floats

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertIsNone(self.calc.divide(7, 0))  # Test division by zero
        self.assertEqual(self.calc.divide(15.6, 3), 5.2)  # Test with floats

if __name__ == "__main__":
    unittest.main()
