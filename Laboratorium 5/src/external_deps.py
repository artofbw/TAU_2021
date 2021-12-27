from hello_world.main import hello_world

from calculator import Calculator


def greeting():
    return hello_world()


def add(x, y):
    calc = Calculator()

    return calc.add(x, y)
