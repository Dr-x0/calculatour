import unittest
from tkinter import Tk
from io import StringIO
import sys

class TestCalculatour(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.calculator = Calculatour(self.root)

    def test_addition(self):
        self.calculator.show(2)
        self.calculator.show('+')
        self.calculator.show(3)
        self.calculator.solve()
        self.assertEqual(self.calculator.equictoin.get(), 5)

    def test_subtraction(self):
        self.calculator.show(5)
        self.calculator.show('-')
        self.calculator.show(3)
        self.calculator.solve()
        self.assertEqual(self.calculator.equictoin.get(), 2)

    def test_clear(self):
        self.calculator.show(9)
        self.calculator.clear()
        self.assertEqual(self.calculator.equictoin.get(), "")

    def tearDown(self):
        self.root.quit()

if __name__ == "__main__":
    unittest.main()
