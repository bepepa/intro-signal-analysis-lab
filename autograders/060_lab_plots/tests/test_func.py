import unittest
from gradescope_utils.autograder_utils.decorators import weight

import numpy as np

# function to test
from post_lab_check import corr_coeff

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass
    
    @weight(1)
    def test_doc_string_present(self):
        """Does the function have a doc string"""
        self.assertGreater(len(corr_coeff.__doc__), 0, "didn't find a doc string")

    @weight(1)
    def test_doc_string_parameter(self):
        """Does the docstring include `Parameters`"""
        self.assertRegexpMatches( corr_coeff.__doc__, 'Parameter', "didn't find `Parameters` in doc string")
    
    @weight(1)
    def test_doc_string_return(self):
        """Does the docstring include `Returns`"""
        self.assertRegexpMatches( corr_coeff.__doc__, 'Return', "didn't find `Returns` in doc string")

    @weight(1)
    def test_corr_real_self(self):
        """correlation coefficient of a real-valued signal with itself"""
        tt = np.arange(0, 10, 1/100)
        xx = np.cos( 2*np.pi*4*tt )
        self.assertAlmostEqual(corr_coeff(xx, xx), 1, msg="correlation coefficient of real-valued signal with itself")
    
    @weight(1)
    def test_corr_complex_self(self):
        """correlation coefficient of a complex-valued signal with itself"""
        tt = np.arange(0, 10, 1/100)
        xx = np.exp( 2j*np.pi*4*tt )
        self.assertAlmostEqual(corr_coeff(xx, xx), 1, msg="correlation coefficient of complex-valued signal with itself")

    @weight(1)
    def test_corr_complex(self):
        """correlation with a complex-valued signal"""
        tt = np.arange(0, 10, 1/100)
        xx = np.exp( 2j*np.pi*4*tt )
        yy = np.ones_like(xx)
        self.assertAlmostEqual(corr_coeff(xx, yy), 0, msg="correlation with first complex valued signal")
        self.assertAlmostEqual(corr_coeff(yy, xx), 0, msg="correlation with second complex valued signal")
        self.assertAlmostEqual(corr_coeff((1+1j)*xx, xx), (1+1j)/np.sqrt(2), msg="correlation with both complex valued signal")

    @weight(1)
    def test_corr_real(self):
        """correlation between real-valued signals"""
        tt = np.arange(0, 10, 1/100)
        xx = np.cos( 2*np.pi*4*tt )
        yy = np.ones_like(xx)
        self.assertAlmostEqual(corr_coeff(xx, yy), 0, msg="correlation between real-valued signals")

    @weight(1)
    def test_raise_if_one_empty(self):
        """raise ValueError when one of the signals is empty"""
        xx = np.array([])
        yy = np.ones(10)
        with self.assertRaises(ValueError):
            corr_coeff(xx, yy)
            corr_coeff(yy, xx)

    @weight(1)
    def test_raise_if_different_length(self):
        """raise ValueError when signals are different length"""
        xx = np.ones(11)
        yy = np.ones(10)
        with self.assertRaises(ValueError):
            corr_coeff(xx, yy)
            corr_coeff(yy, xx)

    @weight(1)
    def test_handles_empty_sig(self):
        """Handles empty signals"""
        xx = np.array([])
        yy = np.ones(10)
        
        self.assertIsNone(corr_coeff(xx, xx), msg="for two empty signals, return `None`")
