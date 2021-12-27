from unittest import TestCase

from src.external_deps import greeting, add


class HelloWorldTestCase(TestCase):

    def test_hello_world_return_greeting(self):
        assert greeting() == "Hello world"


class AddTestCase(TestCase):

    def test_add_return_correct_value(self):
        assert add(3, 4) == '7.00'

    def test_add_return_incorrect_value(self):
        assert add(10, 4) != 12
