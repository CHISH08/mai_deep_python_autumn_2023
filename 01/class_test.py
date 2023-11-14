"""Testing TicTacGame class"""

from game import TicTacGame
import unittest
from io import StringIO
import sys
from unittest.mock import patch


class TestTicTacGame(unittest.TestCase):
    def test_is_correct_input(self):
        game = TicTacGame()
        captured_output = StringIO()
        sys.stdout = captured_output
        self.assertTrue(game.is_correct_input(["1", "2"]))
        self.assertFalse(game.is_correct_input(["1", "2", "3"]))
        self.assertFalse(game.is_correct_input(["a", "b"]))
        self.assertFalse(game.is_correct_input(["3", "2"]))
        self.assertFalse(game.is_correct_input(["-1", "3"]))
        self.assertFalse(game.is_correct_input(["-1", "2."]))
        self.assertFalse(game.is_correct_input(["1,", "2"]))
        self.assertFalse(game.is_correct_input(["1", "0", "2", "1"]))
        self.assertTrue(game.is_correct_input(["2", "1"]))
        self.assertFalse(game.is_correct_input([None, None]))
        self.assertFalse(game.is_correct_input(["", ""]))
        self.assertFalse(game.is_correct_input(["", "1"]))
        self.assertFalse(game.is_correct_input(["1", "afas"]))
        self.assertFalse(game.is_correct_input(["1", "1."]))
        sys.stdout = sys.__stdout__

    def test_check_end(self):
        game = TicTacGame()
        game.matrix = [["X", "-", "-"], ["-", "X", "-"], ["-", "-", "X"]]
        self.assertTrue(game.check_end())
        game.matrix = [["O", "-", "-"], ["O", "-", "-"], ["O", "-", "-"]]
        self.assertTrue(game.check_end())
        game.matrix = [["-", "-", "O"], ["-", "O", "-"], ["O", "-", "-"]]
        self.assertTrue(game.check_end())
        game.matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.assertFalse(game.check_end())
        game.matrix = [["0", "-", "-"], ["X", "X", "-"], ["O", "O", "-"]]
        self.assertFalse(game.check_end())
        captured_output = StringIO()
        sys.stdout = captured_output
        game.counter = 9
        game.people_people_game()
        printed_text = captured_output.getvalue().strip()
        expected_output = "Ничья!\nИгра завершена!"
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_text, expected_output)

    def test_correct_input_start_game(self):
        game = TicTacGame()
        with patch("builtins.input", side_effect=["asfasaw", "0"]):
            self.assertFalse(game.start_game())

        with patch("builtins.input", side_effect=[None, "0"]):
            self.assertFalse(game.start_game())


if __name__ == "__main__":
    unittest.main()
