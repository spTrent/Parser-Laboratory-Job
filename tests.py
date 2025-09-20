from main import *
import unittest


def is_valid_date(date):
    if (len(date) == 8) and (1000 <= int(date[:4]) <= 2025):
        if date[4:6] in ['01', '03', '05', '07', '08', '10', '12']:
            return 1 <= int(date[6:]) <= 31
        elif 2 <= int(date[4:6]) <= 11:
            return 1 <= int(date[6:]) <= 30
    return False

def is_valid_code(code):
    return len(code) == 5 and all(i in '0123456789ABCDEF' for i in code)


class TestParser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nasa(self):
        self.assertTrue(is_valid_date(parser_nasa()))

    def test_rfc(self):
        self.assertTrue(is_valid_date(parser_rfc()))

    def test_unicode(self):
        self.assertTrue(is_valid_code(parser_unicode()))

    def test_bitcoin(self):
        self.assertTrue(is_valid_date(parser_bitcoin()))

    def test_loc(self):
        self.assertTrue(len(parser_loc()) == 10)


if __name__ == '__main__':
    unittest.main()



