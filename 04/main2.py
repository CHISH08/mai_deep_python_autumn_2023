"""
Point 2
"""


class Integer:
    """int"""

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class String:
    """string"""

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class PositiveInteger:
    """uint"""

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be a positive integer")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Data:
    """class for data"""

    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.num}, {self.name}, {self.price}"
