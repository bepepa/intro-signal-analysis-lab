#! /usr/bin/env python3

# File: mse.py
# functions and constants for estimating frequency of a sinsusoid from MSE

import math
import random

# some constants
TRUE_FREQ = 10 + math.sqrt(2.)
FS = 500    # samples per second
NS = 200
SIGMA = 0.1

# generate the signal of interest
tt = [n/FS for n in range(NS)]
SIG = [math.cos(2*math.pi*TRUE_FREQ*t) + random.gauss(0, SIGMA) for t in tt]


def f_mse(freq):
    """Compute the MSE between given signal and sinusoid of frequency freq

    Input:
    -----
    (float) freq - frequency to compute the MSE for

    Returns:
    -------
    (float) MSE
    """
    sig_approx = [math.cos(2*math.pi*freq*t) for t in tt]
    res = sum([(SIG[n] - sig_approx[n])**2 for n in range(len(tt))]) / len(tt)

    return res


def f_me(freq):
    """Compute the mean error between given signal and sinusoid of frequency freq

    Input:
    -----
    (float) freq - frequency to compute the mean error for

    Returns:
    -------
    (float) mean error
    """
    sig_approx = [math.cos(2*math.pi*freq*t) for t in tt]
    res = sum([(SIG[n] - sig_approx[n]) for n in range(len(tt))]) / len(tt)

    return res


def df(freq):
    """Compute the first derivative of MSE with respect to frequency freq

    Input:
    -----
    (float) freq - frequency to compute the mean error for

    Returns:
    -------
    (float) first derivative of MSE
    """
    sig_approx = [math.cos(2 * math.pi * freq * t) for t in tt]
    sin_sig = [math.sin(2 * math.pi * freq * t) for t in tt]
    err = [(SIG[n] - sig_approx[n]) for n in range(len(tt))]

    res = sum([tt[n] * sin_sig[n] * err[n] for n in range(len(tt))]) * 4 * math.pi / len(tt)

    return res


def d2f(freq):
    """Compute the second derivative of MSE with respect to frequency freq

    Input:
    -----
    (float) freq - frequency to compute the mean error for

    Returns:
    -------
    (float) first derivative of MSE
    """
    sig_approx = [math.cos(2 * math.pi * freq * t) for t in tt]
    sin_sq_sig = [(math.sin(2 * math.pi * freq * t)) ** 2 for t in tt]
    cos_sig = [math.cos(2 * math.pi * freq * t) for t in tt]
    err = [(SIG[n] - sig_approx[n]) for n in range(len(tt))]

    res = sum([(tt[n]) ** 2 * (cos_sig[n] * err[n] + sin_sq_sig[n]) for n in range(len(tt))])
    res = res * 2 * (2 * math.pi) ** 2 / len(tt)

    return res


if __name__ == "__main__":
    assert abs( f_me(TRUE_FREQ) ) < SIGMA
    assert f_mse(TRUE_FREQ) < 2*SIGMA
    assert abs( df(TRUE_FREQ) ) < SIGMA
    assert d2f(TRUE_FREQ) > 0
