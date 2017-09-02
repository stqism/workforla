import unittest

from common import util


class FormatCurrencyTestCase(unittest.TestCase):

    def test_formats_integers(self):
        self.assertEqual(util.format_currency(5), '$5')

    def test_adds_commas(self):
        self.assertEqual(util.format_currency(1249826), '$1,249,826')

    def test_formats_floats(self):
        self.assertEqual(util.format_currency(5.25), '$5.25')

    def test_formats_floats_with_no_decimals(self):
        self.assertEqual(util.format_currency(5.0), '$5.00')


if __name__ == '__main__':
    unittest.main()
