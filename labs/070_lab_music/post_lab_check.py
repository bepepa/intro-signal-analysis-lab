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

    #make signal to test with
    fs = 100
    tt = np.arange(0, 1, 1/fs)

    xx = np.array([1, 2, 3, 4, 3, 2, 1])

    # length 2 moving average
    assert np.allclose(moving_average(xx, 2), np.array([1, 3, 5, 7, 7, 5, 3])/2)

    # length 3 moving average
    assert np.allclose(moving_average(xx, 3), np.array([1, 3, 6, 9, 10, 9, 6])/3)

    # check that the proper exception is raised
    try:
        moving_average(xx, 0)
    except ValueError:
        pass

    print("OK")