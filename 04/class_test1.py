import unittest
from main1 import CustomClass

class CustomClassTestCase(unittest.TestCase):
    def test_custom_x(self):
        self.assertEqual(CustomClass.custom_x, 50)

    def test_access_error(self):
        with self.assertRaises(AttributeError):
            CustomClass.x
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            inst.x
        with self.assertRaises(AttributeError):
            inst.val
        with self.assertRaises(AttributeError):
            inst.line()
        with self.assertRaises(AttributeError):
            inst.yyy

    def test_custom_attributes(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_dynamic_attribute(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            inst.dynamic

if __name__ == '__main__':
    unittest.main()