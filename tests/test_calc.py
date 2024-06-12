# test_calc.py
import unittest
from src.calculator import BasicCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = BasicCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5,2), 7)

    def test_previous(self):
        self.calc.add(5,2)
        self.assertEqual(self.calc.return_previous(), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,2),3)

if __name__ == '__main__':
    unittest.main()
