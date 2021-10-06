from unittest import TestCase
from collections import Counter

from photograph import getCounterA, getCounterB


class PhotographTest(TestCase):

    def test_case_3_count_a(self):

        N = 8
        C = ".PBAAP.B"
        X = 1
        Y = 3
        res = getCounterA(N, C, X, Y)
        expected_res = Counter({3: 1, 4: 1})
        self.assertDictEqual(res, expected_res)

    def test_case_3_count_a_reverse(self):

        N = 8
        C = ".PBAAP.B"
        X = 1
        Y = 3
        res = getCounterA(N, C, X, Y, reverse=True)
        expected_res = Counter({3: 1, 4: 1})
        self.assertDictEqual(res, expected_res)
    
    def test_case_3_count_b(self):

        N = 8
        C = ".PBAAP.B"
        X = 1
        Y = 3
        counter_a = Counter({3: 1, 4: 1})
        res = getCounterB(counter_a, N, C, X, Y)
        expected_res = 1
        self.assertEqual(res, expected_res)

    def test_case_3_count_b_reverse(self):

        N = 8
        C = ".PBAAP.B"
        X = 1
        Y = 3
        counter_a = Counter({3: 1, 4: 1})
        res = getCounterB(counter_a, N, C, X, Y, reverse=True)
        expected_res = 2
        self.assertEqual(res, expected_res)
    
    def test_case_1_count_a(self):

        N = 5
        C = "APABA"
        X = 1
        Y = 2
        res = getCounterA(N, C, X, Y)
        expected_res = Counter({0: 0, 2: 1, 4: 0})
        self.assertDictEqual(res, expected_res)

    def test_case_1_count_a_reverse(self):

        N = 5
        C = "APABA"
        X = 1
        Y = 2
        res = getCounterA(N, C, X, Y, reverse=True)
        expected_res = Counter({0: 1, 4: 0, 2: 0})
        self.assertDictEqual(res, expected_res)
    
    def test_case_1_count_b(self):

        N = 5
        C = "APABA"
        X = 1
        Y = 2
        counter_a = Counter({0: 0, 2: 1, 4: 0})
        res = getCounterB(counter_a, N, C, X, Y)
        expected_res = 1
        self.assertEqual(res, expected_res)

    def test_case_1_count_b_reverse(self):

        N = 5
        C = "APABA"
        X = 1
        Y = 2
        counter_a = Counter({0: 0, 4: 0, 2: 0})
        res = getCounterB(counter_a, N, C, X, Y, reverse=True)
        expected_res = 0
        self.assertEqual(res, expected_res)