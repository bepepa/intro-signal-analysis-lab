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

## Copy this cell into the region marked for this Task in the Python file
def corr_coeff(xx, yy):
    """Compute the correlation coefficient between two signals
    
    Parameters:
    -----------
    xx - first signal
    yy - second signal

    Returns:
    --------
    correlation coefficient between the signals

    Note: both signals must have the same length or a `ValueError` will be raised
    """

    ## check inputs
    if len(xx) != len(yy):
        raise ValueError('Signals must be the same length.')
    
    if len(xx) == 0:
        return None
    
    # if we made it to here, arrays are the same length
    numerator = np.sum(xx * np.conjugate(yy))
    denom_sq = np.sum(np.abs(xx)**2) * np.sum(np.abs(yy)**2)

    rho = numerator / np.sqrt(denom_sq)

    return rho

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