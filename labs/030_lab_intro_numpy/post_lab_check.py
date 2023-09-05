#! /usr/bin/env python3
"""
This is the post-lab assessment for lab 3.

See the accompanying notebook for instrutions
"""
import numpy as np

#### Code for setting parameters - leave alone #####
# Parameters for the signals to be synthesized
dur = 1    # signal duration
fs = 100   # sample rate

# first sinusoid
A1 = 2     # amplitude
phi1 = np.pi/4  # phase
f1 = 37    # frequency

# second sinusoid
A2 = 1        # amplitude
phi2 = 0      # frequency
f2 = 0.75     # phase

###########################################################
#   Your code for Task 1 starts here                                 #
###########################################################

tt =     # time grid
s1 =     # first sinusoid
s2 =     # second sinusoid

###########################################################
#   Your code for Task 1 ends here                        #
###########################################################

###########################################################
#   Your code for Task 2 starts here                      #
###########################################################

mean_sq_1 =              # average of the square of the samples in `s1` 
sum_2 =                  # sum of the samples in `s2`
max_12 =                 # largest of the samples in the element-wise product of `s1` and `s2`
mean_abs_1 =             # average of the absolute value of the samples in `s1`
mean_log_2 =             # average of the natural log of the positive (>0) samples in `s2`

###########################################################
#   Your code for Task 2 ends here                        #
###########################################################

#### Code for displaying results - leave alone ########
print(f"Last tt: {tt[-1]:8.4f}")
print(f"Length: {len(s1)}")
print(f"Mean squares 1: {mean_sq_1:8.4f}")
print(f"Sum 2: {sum_2:8.4f}")
print(f"Largest of product: {max_12:8.4f}")
print(f"Mean abs 1: {mean_abs_1:8.4f}")
print(f"Mean log 2: {mean_log_2:8.4f}")