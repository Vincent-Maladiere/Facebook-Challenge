from unittest import TestCase

from rotary import getMinCodeEntryTime


class TestRotary(TestCase):

    def test_case_1(self):

        N = 3
        M = 3
        C = [1, 2, 3]
        res = getMinCodeEntryTime(N, M, C)
        expected_res = 2
        self.assertEqual(res, expected_res)
    
    def test_case_2(self):

        N = 10
        M = 4
        C = [9, 4, 4, 8]
        res = getMinCodeEntryTime(N, M, C)
        expected_res = 11
        self.assertEqual(res, expected_res)

    def test_case_3(self):

        N = 5
        M = 5
        C = [1, 2, 3, 4, 5]
        res = getMinCodeEntryTime(N, M, C)
        expected_res = 4
        self.assertEqual(res, expected_res)
    
    def test_case_4(self):

        N = 1000
        M = 3
        C = [1000, 500, 1]
        res = getMinCodeEntryTime(N, M, C)
        expected_res = 1000
        self.assertEqual(res, expected_res)