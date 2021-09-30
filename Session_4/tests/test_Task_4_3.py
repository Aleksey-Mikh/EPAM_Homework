import unittest

from Session_4.Task_4_3 import rebuild_split


class TestTask(unittest.TestCase):

    def test_case_replace(self):
        string = "Don't forget"
        self.assertEqual(rebuild_split(string), string.split())
        string = "     "
        self.assertEqual(rebuild_split(string), string.split())
        string = '    sad fsd    '
        self.assertEqual(rebuild_split(string), string.split())
        string = "banan naannan"
        self.assertEqual(rebuild_split(string, sep='na'), string.split('na'))
        string = "tot sdf fadtot fdaf rtoot"
        self.assertEqual(rebuild_split(string, sep='tot'), string.split('tot'))


if __name__ == '__main__':
    unittest.main()
