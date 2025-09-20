from parsers import *
import unittest


class TestParser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nasa(self):
        self.assertEqual(parser_nasa(), '19770905')

    def test_rfc(self):
        self.assertEqual(parser_rfc(), '19900401')

    def test_unicode(self):
        self.assertEqual(parser_unicode(), '1F9E0')

    def test_bitcoin(self):
        self.assertEqual(parser_bitcoin(), '20090103')

    def test_loc(self):
        self.assertEqual(parser_loc(), '0131103628')

if __name__ == '__main__':
    unittest.main()



