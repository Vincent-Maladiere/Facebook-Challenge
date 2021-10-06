from unittest import TestCase

from score import getMinProblemCount


class TestScore(TestCase):

    def test_case_1(self):

        N = 6
        S = [1, 2, 3, 4, 5, 6]
        res = getMinProblemCount(N, S)
        expected_res = 4
        self.assertEqual(res, expected_res)

    def test_case_2(self):

        N = 4
        S = [4, 3, 3, 4]
        res = getMinProblemCount(N, S)
        expected_res = 3
        self.assertEqual(res, expected_res)

    def test_case_3(self):

        N = 4
        S = [2, 4, 6, 8]
        res = getMinProblemCount(N, S)
        expected_res = 4
        self.assertEqual(res, expected_res)
