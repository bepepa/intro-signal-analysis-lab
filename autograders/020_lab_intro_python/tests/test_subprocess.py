import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
import random
import sys

SEED = 43

class TestDiff(unittest.TestCase):
    def setUp(self):
        ## collect what the script produces
        self.rec = {}

        script = subprocess.Popen(["python3", "post_lab_check.py", str(SEED)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
        # initialize the random number generator
        random.seed(SEED)

        # and make a list of random numbers
        xx = [random.uniform(0.5, 1.5) for n in range(10)]

        max_v = max(xx)
        min_v = min(xx)
        sum_v = sum(xx)
        avg_v = sum_v / len(xx)

        prod = 1
        for v in xx:
            prod = prod * v

        geo_mean = prod**(1/len(xx))

        self.expected = {
            'Max': max_v,
            'Min': min_v,
            'Sum': sum_v,
            'Arithmetic Mean': avg_v,
            'Product': prod,
            'Geometric Mean': geo_mean,
        }    

    @weight(1)
    def test_max(self):
        """Maximum value"""
        # print(self.expected['Max'], self.rec['Max'])
        k = 'Max'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"Expected {self.expected[k]}, got {self.rec[k]}")
        
    @weight(1)
    def test_min(self):
        """Minimum value"""
        k = 'Min'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"Expected {self.expected[k]}, got {self.rec[k]}")

    @weight(1)
    def test_sum(self):
        """Sum"""
        k = 'Sum'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 3, msg=f"Expected {self.expected[k]}, got {self.rec[k]}")

    @weight(2)
    def test_avg(self):
        """Arithmetic Mean"""
        k = 'Arithmetic Mean'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"Expected {self.expected[k]}, got {self.rec[k]}")

    @weight(3)
    def test_prod(self):
        """Product"""
        k = 'Product'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 3, msg=f"Expected {self.expected[k]}, got {self.rec[k]}")

    @weight(2)
    def test_geo(self):
        """Geometric Mean"""
        k = 'Geometric Mean'
        self.assertAlmostEqual(self.rec[k], self.expected[k], 4, msg=f"Expected {self.expected[k]}, got {self.rec[k]}")
