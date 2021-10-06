from unittest import TestCase

from kaitenzushi import getMaximumEatenDishCount


class TestKaitenzushi(TestCase):

    def test_case_1(self):

        N = 6
        D = [1, 2, 3, 3, 2, 1]
        K = 1
        expected_res = 5
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)
    
    def test_case_2(self):

        N = 6
        D = [1, 2, 3, 3, 2, 1]
        K = 2
        expected_res = 4
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)
    
    def test_case_3(self):

        N = 7
        D = [1, 2, 1, 2, 1, 2, 1]
        K = 2
        expected_res = 2
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)
    
    def test_case_4(self):

        N = 9
        D = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        K = 2
        expected_res = 9
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)

    def test_case_5(self):

        N = 5
        D = [1, 1, 1, 1, 1]
        K = 2
        expected_res = 1
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)

    def test_case_6(self):

        N = 6
        D = [1, 3, 3, 3, 3, 1]
        K = 2
        expected_res = 2
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)

    def test_case_7(self):

        N = 6
        D = [1, 3, 3, 3, 3, 1]
        K = 1
        expected_res = 3
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)

    def test_case_8(self):

        N = 8
        D = [1, 2, 3, 3, 3, 3, 2, 1]
        K = 1
        expected_res = 5
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)

    def test_case_9(self):

        N = 8
        D = [1, 2, 3, 3, 3, 3, 2, 1]
        K = 2
        expected_res = 4
        res = getMaximumEatenDishCount(N, D, K)
        self.assertEqual(expected_res, res)