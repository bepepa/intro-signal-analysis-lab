#! /usr/bin/env python3
"""
This is the post-lab assessment for lab 3.

See the accompanying notebook for instrutions
"""
import numpy as np

###########################################################
#   Your code starts here                                 #
#      paste your function below                          #
###########################################################

def sig_power(xx):
    """Compute the power of the input signal
    
    Parameters
    ----------
    xx - NumPy vector of samples, may be complex-valued

    Returns
    -------
    average power of signal if signal contains at least one sample, otherwise returns `None`
    """
    N = len( xx )

    if N == 0:
        return None
    else:
        return 1/N * np.sum( np.abs(xx)**2 )

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

    # power of a sinusoid is 1/2 * A^2
    assert np.allclose(sig_power(xx), 0.5 * A**2)

    print("OK")