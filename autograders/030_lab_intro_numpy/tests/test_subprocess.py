import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess

import numpy as np


class TestDiff(unittest.TestCase):
    def setUp(self):
        ## collect what the script produces
        self.rec = {}

        script = subprocess.Popen(["python3", "post_lab_check.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            line = script.stdout.readline().rstrip()

            if line:
                # each line is like Max: 0.9801
                # store that as a KV pair in self.rec
                k, v = line.split(':')
                self.rec[k] = float(v)
            else:
                break

        script.terminate()

        ## produce the expected output and store that as well
        ## Parameters for the signals to be synthesized
        dur = 1    # signal duration
        fs = 100   # sample rate

        # first sinusoid
        A1 = 2     # amplitude
        phi1 = np.pi/4  # phase
        f1 = 37    # frequency

        # second sinusoid
        A2 = 1     # amplitude
        phi2 = 0   # frequency
        f2 = 0.75     # phase

        # make signals
        tt = np.arange(0, dur, 1/fs)
        s1 = A1 * np.cos(2*np.pi * f1 * tt + phi1)
        s2 = A2 * np.cos(2*np.pi * f2 * tt + phi2)

        # computations
        mean_sq_1 =  np.mean(s1**2)           # average of the square of the samples in `s1` 
        sum_2 = np.sum(s2)            # sum of the samples in `s2`
        max_12 =  np.max(s1*s2)           # largest of the samples in the element-wise product of `s1` and `s2`
        mean_abs_1 = np.mean(np.abs(s1))            # average of the absolute value of the samples in `s1`
        mean_log_2 = np.mean(np.log(s2[s2 > 0])) 

        self.expected = {
            'Last tt': tt[-1],
            'Length': len(s1),
            'Mean squares 1': mean_sq_1,
            'Sum 2': sum_2,
            'Largest of product': max_12,
            'Mean abs 1': mean_abs_1,
            'Mean log 2': mean_log_2,
        }    

    
    @weight(5)
    def test_signals(self):
        """Signals synthesis"""
        # print(self.expected['Max'], self.rec['Max'])
        k = 'Last tt'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"tt: expected {self.expected[k]}, got {self.rec[k]}")
        k = 'Length'
        self.assertEqual(self.rec[k], self.expected[k], msg="Length of vectors is not right")
        k = 'Mean squares 1'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"s1: expected {self.expected[k]}, got {self.rec[k]}")
        k = 'Sum 2'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"s2: xpected {self.expected[k]}, got {self.rec[k]}")
        
    @weight(1)
    def test_min(self):
        """Sum of squares"""
        k = 'Mean squares 1'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"sum of squares: expected {self.expected[k]}, got {self.rec[k]}")

    @weight(1)
    def test_sum(self):
        """Sum"""
        k = 'Sum 2'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 3, msg=f"sum of s2: expected {self.expected[k]}, got {self.rec[k]}")

    @weight(1)
    def test_lop(self):
        """Largest of Product"""
        k = 'Largest of product'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"largest of product: expected {self.expected[k]}, got {self.rec[k]}")

    @weight(1)
    def test_mabs(self):
        """Mean of absolute valuest"""
        k = 'Mean abs 1'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 3, msg=f"mean of absolute values: expected {self.expected[k]}, got {self.rec[k]}")

    @weight(1)
    def test_mlog(self):
        """Mean of log of positive"""
        k = 'Mean log 2'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"Mean of log of positive: expected {self.expected[k]}, got {self.rec[k]}")
