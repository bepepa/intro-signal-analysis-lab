"""Module containing functions from the pre-lab notebook"""

import numpy as np
import matplotlib.pyplot as plt

def synthesize_from_vector(Xvec):
    """Synthesize a signal from its spectrum
    
    Parameters:
    -----------
    Xvec - a length N vector representation of the spectrum

    Returns
    -------
    NumPy array containing the signal
    """
    N = len(Xvec)
    xx = np.zeros_like(Xvec)

    for k in range(-N//2, N//2):
        cplx_exp = np.exp(2j*np.pi * k/N * np.arange(N))
        xx = xx + Xvec[k + N//2] * cplx_exp

    return xx


def analyze_signal(xx):
    """Analyze a signal to find its spectrum
    
    Parameters:
    -----------
    xx - a length N sampled signal

    Returns
    -------
    NumPy array containing the spectrum
    """
    N = len(xx)
    Xvec = np.zeros_like(xx, dtype=complex)

    for n in range(N):
        cplx_exp = np.exp(-2j*np.pi * n/N * np.arange(-N//2, N//2))
        Xvec = Xvec + xx[n] * cplx_exp

    return 1/N * Xvec


def plot_spectrum(Xv, fs, doStem=False):
    """Plot magnitude and phase of the spectrum"""

    N = len(Xv)
    ff = np.arange(-N/2, N/2, 1) * fs/N

    fig, (axm, axp) = plt.subplots(2, 1, layout='constrained')
    
    if doStem:
        axm.stem(ff, np.abs(Xv))
    else:
        axm.semilogy(ff, np.abs(Xv))
    axm.grid()
    axm.set_ylabel('Magnitude')

    if doStem:
        axp.stem(ff, np.angle(Xv)/np.pi)
    else:
        axp.plot(ff, np.angle(Xv)/np.pi)
    axp.set_xlabel('Frequency (Hz)')
    axp.set_ylabel('Phase (rad/$\pi$)')
    axp.grid()

    plt.show()