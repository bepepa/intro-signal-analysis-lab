import unittest
from gradescope_utils.autograder_utils.decorators import weight

import numpy as np

# function to test
from post_lab_check import moving_average

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass
    
    @weight(1)
    def test_doc_string_present(self):
        """Does the function have a doc string"""
        self.assertGreater(len(moving_average.__doc__), 0, "didn't find a doc string")

    @weight(1)
    def test_doc_string_parameter(self):
        """Does the docstring include `Parameters`"""
        self.assertRegexpMatches( moving_average.__doc__, 'Parameter', "didn't find `Parameters` in doc string")
    
    @weight(1)
    def test_doc_string_return(self):
        """Does the docstring include `Returns`"""
        self.assertRegexpMatches( moving_average.__doc__, 'Return', "didn't find `Returns` in doc string")

    @weight(2)
    def test_real_ma(self):
        """moving average of a real-valued input"""
        tt = np.arange(0, 10, 1/100)
        xx = np.cos( 2*np.pi*4*tt )
        N = len(xx)

        for M in range(1, 5):
            yy = moving_average(xx, M)
            zz = np.convolve(xx, np.ones(M)/M)[:N]

            self.assertTrue(np.allclose(yy,zz), msg="moving average of real-valued signal")
    
    @weight(2)
    def test_complex_ma(self):
        """moving average of a complex-valued input"""
        tt = np.arange(0, 10, 1/100)
        xx = np.exp( 2j*np.pi*4*tt )
        N = len(xx)

        for M in range(1, 5):
            yy = moving_average(xx, M)
            zz = np.convolve(xx, np.ones(M)/M)[:N]

            self.assertTrue(np.allclose(yy,zz), msg="moving average of complex-valued signal")

    @weight(1)
    def test_empty_sig(self):
        """Empty input signal"""
        xx = np.array([])

        yy = moving_average(xx, 2)

        self.assertTrue(len(yy) == len(xx), msg="Empty input signal")

    
    @weight(2)
    def test_raise_if_M_leq_0(self):
        """raise ValueError when M is less than or equal to 0"""
        xx = np.ones(10)
        with self.assertRaises(ValueError):
            moving_average(xx, 0)
            moving_average(xx, -1)

    