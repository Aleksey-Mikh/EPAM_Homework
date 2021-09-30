import unittest

from Session_4.Task_4_5 import get_digits


class TestTask(unittest.TestCase):

    def test_case_replace(self):
        self.assertEqual(get_digits(982), (9, 8, 2))
        self.assertEqual(get_digits(9585882), (9, 5, 8, 5, 8, 8, 2))


if __name__ == '__main__':
    unittest.main()
