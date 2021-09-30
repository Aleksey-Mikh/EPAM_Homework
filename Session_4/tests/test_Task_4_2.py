import unittest
from unittest.mock import patch

from Session_4.Task_4_2 import get_clear_string, find_palindrome


class TestTask(unittest.TestCase):

    def test_case_replace(self):
        string = "Mr. Owl ate my metal worm"
        string_correct = "mrowlatemymetalworm"
        self.assertEqual(get_clear_string(string), string_correct)
        string = "Anna"
        string_correct = "anna"
        self.assertEqual(get_clear_string(string), string_correct)

    @patch('builtins.print')
    def test_case_palindrome(self, mock_print):
        """check console print"""
        string = "mrowlatemymetalworm"
        find_palindrome(string)
        mock_print.assert_called_with("String is a palindrome")

        string = "anna"
        find_palindrome(string)
        mock_print.assert_called_with("String is a palindrome")

        string = "anua"
        find_palindrome(string)
        mock_print.assert_called_with("String is not a palindrome")


if __name__ == '__main__':
    unittest.main()
