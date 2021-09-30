import unittest

from Session_4.Task_4_1 import replace_quotation_marks


class TestTask(unittest.TestCase):

    def test_case_replace(self):
        string = "Don't forget"
        string_correct = "Don\"t forget"
        self.assertEqual(replace_quotation_marks(string), string_correct)
        string = "\"Don't forget,\" said John. \"As Mr. B said, " \
                 "\"it's mandarin, not margarine'.\""
        string_correct = "'Don\"t forget,' said John. 'As Mr. B said, " \
                         "'it\"s mandarin, not margarine\".'"
        self.assertEqual(replace_quotation_marks(string), string_correct)


if __name__ == '__main__':
    unittest.main()
