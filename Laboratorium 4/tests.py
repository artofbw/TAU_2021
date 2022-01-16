from unittest import TestCase
from unittest.mock import patch

from example import Example


class ExampleTestCase(TestCase):

    @patch('example.Example.a', return_value=0)
    def test_example_mocked_a_return_default_value(self, mocked_example):
        example = Example()

        returned_value = example.a()

        mocked_example.assert_called_once()
        self.assertEqual(returned_value, 0)

    @patch('example.Example.a', return_value="test")
    def test_example_mocked_a_return_string(self, mocked_example):
        example = Example()

        returned_value = example.a()

        mocked_example.assert_called_once()
        self.assertEqual(returned_value, "test")

    @patch('example.Example.b', return_value=100)
    def test_example_mocked_b_return_int(self, mocked_example):
        example = Example()

        returned_value = example.b()

        mocked_example.assert_called_once()
        self.assertEqual(returned_value, 100)


class CalculatorTestCase(TestCase):

    @patch('calculator.Calculator.sum', return_value=9)
    def test_sum(self, mocked_sum):
        self.assertEqual(mocked_sum(2, 3), 9)

    @patch('calculator.Calculator.sum', return_value="test")
    def test_sum_return_string(self, mocked_sum):
        self.assertEqual(mocked_sum(2, 3), "test")

    @patch('calculator.Calculator.sum', return_value=["element1", "element2"])
    def test_sum_return_list(self, mocked_sum):
        self.assertEqual(mocked_sum(2, 3), ["element1", "element2"])
