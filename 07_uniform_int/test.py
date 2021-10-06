from unittest import TestCase

from uniform import getUniformIntegerCountInInterval


class TestUniform(TestCase):

    def test_case_1(self):

        A = 75
        B = 300
        res = getUniformIntegerCountInInterval(A, B)
        res_expected = 5
        self.assertEqual(res, res_expected)

    def test_case_2(self):

        A = 1
        B = 9
        res = getUniformIntegerCountInInterval(A, B)
        res_expected = 9
        self.assertEqual(res, res_expected)

    def test_case_1(self):

        A = 999999999999
        B = 999999999999
        res = getUniformIntegerCountInInterval(A, B)
        res_expected = 1
        self.assertEqual(res, res_expected)