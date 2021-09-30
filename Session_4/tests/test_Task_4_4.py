import unittest

from Session_4.Task_4_4 import split_by_index


class TestTask(unittest.TestCase):

    def test_case_replace(self):
        string = "pythoniscool,isn'tit?"
        ind = [6, 8, 12, 13, 18]
        correct = ['python', 'is', 'cool', ',', "isn't", 'it?']
        self.assertEqual(split_by_index(string, ind), correct)
        string = "pythoniscool"
        ind = [2, 8, 15]
        correct = ['py', 'thonis', 'cool']
        self.assertEqual(split_by_index(string, ind), correct)


if __name__ == '__main__':
    unittest.main()
