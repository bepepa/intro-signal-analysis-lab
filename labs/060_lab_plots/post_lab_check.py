#! /usr/bin/env python3
"""
This is the post-lab assessment for lab 6.

See the accompanying notebook for instrutions


IMPORTANT: This file MUST be named `post_lab_check.py` 
"""
import numpy as np

###########################################################
#   Your code starts here                                 #
#      paste your function below                          #
###########################################################



###########################################################
#   Your code ends here                                   #
###########################################################


# the code below allows you to run this file like a script for testing
# The only output should be the word 'OK'
if __name__ == "__main__":

    #make a signal to test with
    fs = 100
    tt = np.arange(0, 1, 1/fs)

    A = 3
    f = 5
    phi = np.pi/7

    xx = A * np.cos(2*np.pi * f * tt + phi)

    # correlation of signal with itself is 1
    assert np.allclose(corr_coeff(xx, xx), 1)

    # correlation of signal with negative of itself is -1
    assert np.allclose(corr_coeff(xx, -xx), -1)

    # correlation between xx and an all-1s signal
    yy = np.ones_like(xx)
    assert np.allclose(corr_coeff(xx, yy), 0)

    # check that the proper exception is raised
    try:
        corr_coeff(xx, xx[1:])
    except ValueError:
        pass

    print("OK")