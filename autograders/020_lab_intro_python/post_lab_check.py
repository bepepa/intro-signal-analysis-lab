#! /usr/bin/env python3
"""
This is the post-lab assessment for lab 2.

Your task is to complete the code below as indicated. Your task is to compute
for a given list (stored as `xx`) containing positive floating point numbers:
* the minimum value
* the maximum value
* the sum of all values
* the arithmetic mean (average)
* the product of all values
* the geometric mean
"""
#### Code for generating the list - leave alone #####
import sys
import random

if len(sys.argv) == 1:
    seed = 42
else:
    seed = int(sys.argv[1])

# initialize the random number generator
random.seed(seed)

# and make a list of random numbers
xx = [random.uniform(0.5, 1.5) for n in range(10)]

###########################################################
#   Your code starts here                                 #
###########################################################

max_v = max(xx)
min_v = min(xx)
sum_v = sum(xx)
avg_v = sum_v / len(xx)

prod = 1
for v in xx:
    prod = prod * v

geo_mean = prod**(1/len(xx))

###########################################################
#   Your code ends here                                   #
###########################################################
print(f"Max: {max_v:6.4f}")
print(f"Min: {min_v:6.4f}")
print(f"Sum: {sum_v:6.3f}")
print(f"Arithmetic Mean: {avg_v:6.4f}")
print(f"Product: {prod:6.3f}")
print(f"Geometric Mean: {geo_mean:6.4f}")

