#!/usr/bin/env python3

import unittest
import cal


class TestCal(unittest.TestCase):

    def setUp(self):
        self.test_string = '   February 2014\nSu Mo Tu We Th Fr Sa\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28\n'
        self.test_string2 = '    August 2019\nMo Tu We Th Fr Sa Su\n          1  2  3  4\n 5  6  7  8  9 10 11\n12 13 14 15 16 17 18\n19 20 21 22 23 24 25\n26 27 28 29 30 31\n'

    def test_cal(self):
        self.assertEqual(cal.cal(2, 2014, 6), self.test_string)
        self.assertEqual(cal.cal(8, 2019, 0), self.test_string2)
        self.assertRaises(SystemExit, cal.parse_input, 33, 2300, 0)
        self.assertRaises(SystemExit, cal.parse_input, 4, 23000, 0)

    def test_parse_input(self):
        self.assertEqual(cal.parse_input('2', '2014', 'Montag'), (2, 2014, 0))
        self.assertEqual(cal.parse_input('2', '2014', 'sonntag'), (2, 2014, 6))
        self.assertRaises(SystemExit, cal.parse_input, 'foo', 'bar', 0)
        self.assertRaises(SystemExit, cal.parse_input, '4', '2', 0)

    def test_parse_weekday(self):
        self.assertEqual(cal.parse_weekday('montag'), 0)
        self.assertEqual(cal.parse_weekday('Montag'), 0)
        self.assertEqual(cal.parse_weekday('Sonntag'), 6)
        self.assertEqual(cal.parse_weekday('mittwoch'), 2)
        self.assertEqual(cal.parse_weekday('foobar'), None)

    def test_myargparse(self):
        self.assertRaises(SystemExit, cal.myargparse, ['script', 'foo', 12, 'bar'])
        self.assertRaises(SystemExit, cal.myargparse, ['script', 8, 2019, 'bar'])
        self.assertEqual(cal.myargparse(('script', 8, 3019, 'Montag')), None)


if __name__ == '__main__':
    unittest.main()
