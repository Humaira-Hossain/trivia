import builtins
from unittest import TestCase, main
from unittest.mock import Mock, patch
from funcs import *


class TestNumberOfQuestions(TestCase):
    @patch('builtins.input', side_effect=['4'])
    def test_valid_input(self, mock_input):
        expected = 4
        actual = number_of_questions()

        self.assertEqual(expected, actual)

    def test_another_valid_input(self):
        with patch("builtins.input", side_effect=["1"]):
            expected = 1
            result = number_of_questions()

            self.assertEqual(expected, result)

    def test_q_input_system_exit(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["   q"]

            number_of_questions()

    def test_quit_input_system_exit(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["qUit   "]

            number_of_questions()

    @patch('builtins.input', side_effect=['0'])
    def test_0_input_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            number_of_questions()

    @patch('builtins.input', side_effect=[''])
    def test_empty_input_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            number_of_questions()

    @patch('builtins.input', side_effect=['2.5'])
    def test_float_input_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            number_of_questions()


class TestDifficulty(TestCase):
    def test_input_1_valid(self):
        with patch("builtins.input", side_effect=["1"]):
            expected = 'easy'
            result = difficulty()

            self.assertEqual(expected, result)

    def test_input_hard_valid(self):
        with patch("builtins.input", side_effect=["hard"]):
            expected = 'hard'
            result = difficulty()

            self.assertEqual(expected, result)

    @patch('builtins.input', side_effect=['2.5'])
    def test_float_input_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            difficulty()

    @patch('builtins.input', side_effect=['5'])
    def test_large_input_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            difficulty()

    @patch('builtins.input', side_effect=['e'])
    def test_letter_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            difficulty()

    @patch('builtins.input', side_effect=[''])
    def test_empty_raises_value_error(self, mock_input):
        with self.assertRaises(Exception):
            difficulty()

    def test_quit_input_system_exit(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["qUit   "]

            difficulty()

    def test_q_input_system_exit(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["q"]

            difficulty()

    def test_4_input_system_exit(self):
        with self.assertRaises(SystemExit):
            builtins.input = Mock()
            builtins.input.side_effect = ["4"]

            difficulty()


class TestGetEndpoint(TestCase):
    def test_get_endpoint(self):
        num = 3
        diff = 'easy'
        expected = f'https://the-trivia-api.com/api/questions?limit={num}&difficulty={diff}'
        actual = get_endpoint(num, difficulty)

        self.assertEqual(expected, actual)


class TestGetJson(TestCase):
    pass


class TestGetQuestions(TestCase):
    pass


class TestGetCorrectAnswers(TestCase):
    pass


class TestGetOptions(TestCase):
    pass


class TestDisplayQuestions(TestCase):
    pass


class TestDisplayOptions(TestCase):
    pass


class TestUserAnswer(TestCase):
    pass


class TestIsCorrect(TestCase):
    pass


class TestPlayAgain(TestCase):
    pass
