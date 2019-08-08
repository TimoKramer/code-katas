#!/usr/bin/env python3

import unittest
import to_roman

class TestToRoman(unittest.TestCase):

    def test_decimal_to_roman(self):
        self.assertEqual(to_roman.decimal_to_roman(1), 'I')
        self.assertEqual(to_roman.decimal_to_roman(2), 'II')
        self.assertEqual(to_roman.decimal_to_roman(4), 'IV')
        self.assertEqual(to_roman.decimal_to_roman(5), 'V')
        self.assertEqual(to_roman.decimal_to_roman(9), 'IX')
        self.assertEqual(to_roman.decimal_to_roman(10), 'X')
        self.assertEqual(to_roman.decimal_to_roman(42), 'XLII')
        self.assertEqual(to_roman.decimal_to_roman(99), 'XCIX')
        self.assertEqual(to_roman.decimal_to_roman(2013), 'MMXIII')


if __name__ == '__main__':
    unittest.main()

