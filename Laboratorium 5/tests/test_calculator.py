from unittest import TestCase

from src.calculator import add, subtract, multiply, divide


class CalculatorTestCase(TestCase):

    def test_calculator_add_returns_correct_value(self):
        assert add(5, 5) == 10

    def test_calculator_add_returns_wrong_value(self):
        assert add(5, 5) != 1

    def test_calculator_subtract_returns_correct_value(self):
        assert subtract(5, 5) == 0

    def test_calculator_subtract_returns_wrong_value(self):
        assert subtract(5, 5) != 1

    def test_calculator_multiply_returns_correct_value(self):
        assert multiply(5, 5) == 25

    def test_calculator_multiply_returns_wrong_value(self):
        assert multiply(5, 5) != 1

    def test_calculator_divide_returns_correct_value(self):
        assert divide(5, 5) == 1

    def test_calculator_divide_returns_wrong_value(self):
        assert divide(5, 5) != 5
