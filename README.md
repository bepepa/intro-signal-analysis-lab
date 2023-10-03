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
[View the pre-lab notebook for lab 3](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/030_lab_intro_numpy/pre_lab_notes.ipynb)</br>
[View the notebook for lab 3](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/030_lab_intro_numpy/lab.ipynb)
* **Lab 4 - Writing Functions:** Digital Signal Processing often involves transforming aninput signal into an output signal. This is best accomplished by writing a function that accepts a signal as an input and produces a signal as the output from the function. You will learn how to write functions in Python.
[View the pre-lab notebook for lab 4](https://nbviewer.org/format/slides/github/bepepa/intro-signal-analysis-lab/blob/main/labs/040_lab_functions/pre_lab_notes.ipynb)</br>
[View the notebook for lab 4](https://nbviewer.org/github/bepepa/intro-signal-analysis-lab/blob/main/labs/040_lab_functions/lab.ipynb)
* **Lab 5 - Translating Signal Processing Math to Code:** In our lectures, we often see expressions like
$$
x[n] = \sum_{k} X_k \cdot e^{j2\pi f_k n/f_s} \text{, for $n=0, 1, ..., N$.}
$$
[View the pre-lab notebook for lab 5](https://nbviewer.org/github/bepepa/intro-signal-analysis-lab/blob/main/labs/050_lab_math/pre_lab_notes.ipynb)</br>
[View the notebook for lab 5](https://nbviewer.org/github/bepepa/intro-signal-analysis-lab/blob/main/labs/050_lab_math/lab.ipynb)

You will learn how to interpret such expressions and translate them to Python code using NumPy functions.
* **Lab 6 - Plotting with Matplotlib:** The [MatplotLib](https://matplotlib.org/) module provides a powerful set of functions that make it straightforward to produce publication-quality plots and graphics.</br>
[View the pre-lab notebook for lab 6](https://nbviewer.org/github/bepepa/intro-signal-analysis-lab/blob/main/labs/060_lab_plots/pre_lab_notes.ipynb)</br>
[View the notebook for lab 6](https://nbviewer.org/github/bepepa/intro-signal-analysis-lab/blob/main/labs/060_lab_plots/lab.ipynb)

* **Lab 7 - Synthesizing Music:** In this two-week lab, you learn to generate signals for a (well-known) music piece. This lab is derived from [one of the labs in our textbook](https://dspfirst.gatech.edu/chapters/DSP1st2eLabs/MusicSynthLab.pdf).
