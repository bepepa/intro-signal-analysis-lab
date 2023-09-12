import unittest
from gradescope_utils.autograder_utils.decorators import weight

import numpy as np

# function to test
from post_lab_check import sig_power

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass
    
    @weight(1)
    def test_doc_string_present(self):
        """Does the function have a doc string"""
        self.assertGreater(len(sig_power.__doc__), 0, "didn't find a doc string")

    @weight(1)
    def test_doc_string_parameter(self):
        """Does the docstring include `Parameters`"""
        self.assertRegexpMatches( sig_power.__doc__, 'Parameter', "didn't find `Parameters` in doc string")
    
    @weight(1)
    def test_doc_string_return(self):
        """Does the docstring include `Returns`"""
        self.assertRegexpMatches( sig_power.__doc__, 'Return', "didn't find `Returns` in doc string")

    @weight(2)
    def test_power_real(self):
        """power of a real-valued signal"""
        tt = np.arange(0, 10, 1/100)
        xx = np.cos( 2*np.pi*3*tt )
        self.assertAlmostEqual(sig_power(xx), 0.5, msg="power of real-valued signals")

    @weight(2)
    def test_power_complex(self):
        """power of a complex-valued signal"""
        tt = np.arange(0, 10, 1/100)
        xx = np.exp( 2j*np.pi*3*tt )
        self.assertAlmostEqual(sig_power(xx), 1, msg="power of real-valued signals")

    @weight(1)
    def test_real_power(self):
        """Is the power of a coplex signal real-valued?"""
        tt = np.arange(0, 10, 1/100)
        xx = np.exp( 2j*np.pi*3*tt )
        self.assertTrue(isinstance( sig_power(xx), float), msg="is power of complex signal real?")

    @weight(2)
    def test_handles_empty_sig(self):
        """Handles an empty signal"""
        xx = np.array([])
        self.assertIsNone(sig_power(xx), msg="for empty signals, return `None`")
