"""
Point 1
"""


class CustomMeta(type):
    """Metaclass"""

    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith("__"):
                new_attrs[f"custom_{attr_name}"] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(mcs, name, bases, new_attrs)


class CustomClass(metaclass=CustomMeta):
    """Customclass"""

    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """function calss"""
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

    def __setattr__(self, name, val):
        if not name.startswith("__"):
            return super().__setattr__("custom_" + name, val)
        return super().__setattr__(name, val)
