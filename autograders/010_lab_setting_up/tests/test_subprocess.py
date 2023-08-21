import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
import re


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    def test_no_args(self):
        """The only test:  just verify the script output"""
        script = subprocess.Popen(["python3", "my_first_script.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = script.stdout.read().strip().decode()
        
        p = re.compile(r"Hello\s*(.*)\s*!")
        m = p.match(output)

        self.assertIsNotNone(m, "The expected output is of the form 'Hello YOUR_NAME !")
        
        err = script.stderr.read().strip()
        referenceOutput = b""
        self.assertEqual(err, referenceOutput)
        
        script.terminate()

    