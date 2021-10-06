from unittest import TestCase

from stack import getMinimumDeflatedDiscCount


class TestStack(TestCase):

    def test_case_1(self):

        N = 5
        R = [2, 5, 3, 6, 5]
        res = getMinimumDeflatedDiscCount(N, R)
        res_expected = 3
        self.assertEqual(res, res_expected)
    
    def test_case_2(self):

        N = 3
        R = [100, 100, 100]
        res = getMinimumDeflatedDiscCount(N, R)
        res_expected = 2
        self.assertEqual(res, res_expected)

    def test_case_2(self):

        N = 4
        R = [6, 5, 4, 3]
        res = getMinimumDeflatedDiscCount(N, R)
        res_expected = -1
        self.assertEqual(res, res_expected)