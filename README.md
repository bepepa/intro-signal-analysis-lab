# Introduction to Signal Analysis Labs

This repository holds the [Python](https://python.org) based lab assignments for the course "Introduction to Signal Analysis" at George Mason University.
Only the foundational labs (labs 1-8) are included here. The semester project will be provided in a separate repository.

## Lab Topics

* **Lab 1 - Getting started:** you will learn to set up, configure, and use the tools needed for the lab, including [Anaconda](https://www.anaconda.org/). You will learn the difference between Python scripts and Jupyter notebooks - both of which will be used throughout this class.</br>
[View the notebook for lab 1](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/010_lab_setting_up/setting_up.ipynb)
* **Lab 2 - Python:** after a refresher on the Python language, we will explore a method to estimate the frequency of a (noisy) sinusoid very accurately.</br>
[View the pre-lab notebook for lab 2](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/020_lab_intro_python/pre_lab_notes.ipynb)</br>
[View the notebook for lab 2](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/020_lab_intro_python/lab.ipynb)
* **Lab 3 - NumPy and Matplotlib:** you will learn that the [`NumPy`](https://numpy.org) package greatly simplifies generating and processing discrete-time signals. Using NumPy, we will experiment with sinusoidal signals</br>
[View the pre-lab notebook for lab 2](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/030_lab_intro_numpy/pre_lab_notes.ipynb)</br>
[View the notebook for lab 2](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/030_lab_intro_numpy/lab.ipynb)
* **Lab 4 - Translating Signal Processing Math to Code:** In our lectures, we often see expressions like
```math
y[n] = \sum_{k=0}^{M-1} h[k] \cdot x[n-k] \text{, for $n=0, 1, ..., N$.}
```
You will learn how to interpret such expressions and translate them to Python code using NumPy functions.
* **Lab 5 - Writing Functions:** Digital Signal Processing often involves transforming aninput signal into an output signal. This is best accomplished by writing a function that accepts a signal as an input and produces a signal as the output from the function. You will learn how to write functions in Python.
* **Lab 6 - Interacting with the World:** To be useful, signal processing systems must be able to accept signals from the real world. You will learn how to read signals from a file, a device, or from the network and to write processed signals back to a file or an output device.
* **Lab 7 - Signal Processing Functions in NumPy and SciPy:** You will learn that the [`NumPy`](https://numpy.org) and [`SciPy`](https://scipy.org) packages provide a wealth of signal processing functions that can be used as building blocks for signal processing systems.
* **Lab 8 - Signal Processing Systems:** Combining signals from the real world and signal, processing functions, we can construct signal processing systems. You will learn how to combine signal processing functions to create larger systems for processing real world signals.
