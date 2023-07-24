# Introduction to Signal Analysis Labs

This repository holds the Python based lab assignments for the course "Introduction to Signal Analysis" at George Mason University.
Only the foundational labs (labs 1-7) are included here. The semester project is provided in a separate repository.

## Lab Topics

* **Lab 1 - Getting started:** you will learn to set up, configure, and use the tools needed for the lab, including PyCharm. You will learn the difference between Python scripts and Jupyter notebooks - both of which will be used throughout this class.
* **Lab 2 - Python:** after a brief refresher on the Python language, you will learn how to use Python and the `math` module of the standard library to generate sinusoidal signals.
* **Lab 3 - NumPy and MatPlotlib:** you will learn that the `NumPy` package greatly simplifies generating and processing discrete-time signals. The functions in the `MatPlotlib` package let you visualize (plot) signals.
* **Lab 4 - Translating Signal Processing Math to Code:** In our lectures, we often see expressions like this
$$
y[n] = \sum_{k=0}^{M-1} h[k] \cdot x[n-k] \text{, for $n=0, 1, ..., N$.}
$$
You will learn how to interpret such expressions and translate them to Python code using NumPy functions.
* **Lab 5 - Writing Functions:** Digital Signal Processing often involves transforming aninput signal into an output signal. This is best accomplished by writing a function that accepts a signal as an input and produces a signal as the output from the function. You will learn how to write functions in Python.
* **Lab 6 - Interacting with the World:** To be useful, signal processing systems must be able to accept signals from the real world. You will learn how to read signals from a file, a device, or from the network and to write processed signals back to a file or an output device.
* **Lab 7 - Signal Processing Functions in NumPy and SciPy:** You will learn that the `NumPy` and `SciPy` packages provide a wealth of signal processing functions that can be used as building blocks for signal processing systems.
* **Lab 8 - Signal Processing Systems:** Combining signals from the real world and signal, processing functions, we can construct signal processing systems. You will learn how to combine signal processing functions to create larger systems for processing real world signals.
