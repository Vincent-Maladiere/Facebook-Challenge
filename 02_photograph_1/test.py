from unittest import TestCase
from unittest.case import expectedFailure

from photograph import getArtisticPhotographCount


class PhotographTest(TestCase):

    has_fail = True

    def print_debug(self, res, expected_res, **params):

        if not self.has_fail and res != expected_res:
            getArtisticPhotographCount(**params)
            self.has_fail = True
    
    def test_case_1(self):

        N = 5
        C = "APABA"
        X = 1
        Y = 2
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 1)
    
    def test_case_2(self):

        N = 5
        C = "APABA"
        X = 2
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 0)
    
    def test_case_3(self):

        N = 8
        C = ".PBAAP.B"
        X = 1
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 3)
    
    def test_case_4(self):

        C = "PPBBAABBPP"
        N = 10
        assert len(C) == 10
        X = 1
        Y = 4
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 12)

    def test_case_5(self):

        C = "BA..PP..AB"
        N = len(C)
        X = 1
        Y = 1
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 0)

    def test_case_6(self):

        C = "BA..PP..AB"
        N = len(C)
        X = 2
        Y = 2
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 0)
    
    def test_case_7(self):

        C = "BA..PP..AB"
        N = len(C)
        X = 3
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 0)
    
    def test_case_8(self):

        C = "BA..PP..AB"
        N = len(C)
        X = 1
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 2)

    def test_case_9(self):

        C = "BA..PP..AB"
        N = len(C)
        X = 1
        Y = 4
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 4)

    def test_case_10(self):

        C = "BA..PP..AB"
        N = len(C)
        X = 1
        Y = 10
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 4)
        
    def test_case_11(self):

        C = "PABPABPAB"
        N = len(C)
        X = 1
        Y = 1
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 3)

    def test_case_12(self):

        C = "PABPABPAB"
        N = len(C)
        X = 1
        Y = 2
        result = getArtisticPhotographCount(N, C, X, Y)
        self.assertEqual(result, 4)

    def test_case_13(self):

        C = "PABPABPAB"
        N = len(C)
        X = 1
        Y = 4
        result = getArtisticPhotographCount(N, C, X, Y)
        expected_sol = 9
        self.print_debug(result, expected_sol, **dict(C=C, N=N, X=X, Y=Y, v=True))
        self.assertEqual(result, expected_sol)
    
    def test_case_14(self):

        C = "PPAABB..PPAABB"
        N = len(C)
        X = 1
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        expected_sol = 16
        self.print_debug(result, expected_sol, **dict(C=C, N=N, X=X, Y=Y, v=True))
        self.assertEqual(result, expected_sol)

    def test_case_15(self):

        C = "PAB" * 60
        N = len(C)
        X = 1
        Y = 1
        result = getArtisticPhotographCount(N, C, X, Y)
        expected_sol = 60
        self.print_debug(result, expected_sol, **dict(C=C, N=N, X=X, Y=Y, v=True))
        self.assertEqual(result, expected_sol)

    def test_case_16(self):

        C = "..PABPABPAB.." * 30
        N = len(C)
        X = 1
        Y = 4
        result = getArtisticPhotographCount(N, C, X, Y)
        expected_sol = 9 * 30
        self.print_debug(result, expected_sol, **dict(C=C, N=N, X=X, Y=Y, v=True))
        self.assertEqual(result, expected_sol)

    def test_case_17(self):

        C = "P.A.B.P.A.B"
        N = len(C)
        X = 3
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        expected_sol = 0
        self.print_debug(result, expected_sol, **dict(C=C, N=N, X=X, Y=Y, v=True))
        self.assertEqual(result, expected_sol)

    def test_case_18(self):

        C = "P..A..B"
        N = len(C)
        X = 3
        Y = 3
        result = getArtisticPhotographCount(N, C, X, Y)
        expected_sol = 1
        self.print_debug(result, expected_sol, **dict(C=C, N=N, X=X, Y=Y, v=True))
        self.assertEqual(result, expected_sol)
