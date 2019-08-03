#!/usr/bin/env python3

import unittest
import itertools

import bankocr


class TestBankOCR(unittest.TestCase):

    def test_take_lines(self):
        with open('test.txt') as f:
            self.assertIsInstance(bankocr.take_lines(f), itertools.islice)
            self.assertEquals(list(bankocr.take_lines(f))[1], '  | _| _||_||_ |_   ||_||_|\n')

    def test_char(self):
        self.assertEqual(list(list(bankocr.take_char(['foobar']))[0]), ['f', 'o', 'o'])
        self.assertEqual(list(list(bankocr.take_char(['foobar']))[0]), ['f', 'o', 'o'])

    def test_parse_char(self):
        self.assertIsNot(bankocr.parse_char('     |  |'), 2)
        self.assertIsNone(bankocr.parse_char('        |'), 2)
        self.assertIs(bankocr.parse_char(' _  _||_ '), 2)

if __name__ == '__main__':
    unittest.main()
