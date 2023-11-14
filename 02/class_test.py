import unittest
from unittest.mock import patch
import main


class TestMyFunctionCallCount(unittest.TestCase):
    @patch("main.parse_json")
    def test_my_function_call_count(self, mock_function):
        main.param = 4
        main.main(3)
        main.param = 3
        main.main(2)
        main.param = 5
        main.main(10)
        self.assertEqual(mock_function.call_count, 15)


if __name__ == "__main__":
    unittest.main()
