#!/usr/bin/env python3

import unittest
import cal

class TestCal(unittest.TestCase):

    def setUp(self):
        self.test_string = '   February 2014\nSu Mo Tu We Th Fr Sa\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28\n'

    def test_cal(self):
        self.assertEqual(cal.cal(2, 2014, 6), self.test_string)

if __name__ == '__main__':
    unittest.main()
