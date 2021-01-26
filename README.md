[![Build Status](https://travis-ci.com/chapman-phys220-2018f/cw07-late_for_class.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/cw07-late_for_class)

**Author(s):** **Amelia Roseto**

## Specification

1. Go through the python code in the repository showing the reference list implementation of the Gaussian function: $$g(x) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{x^2}{2} \right).$$ Make sure you observe how the python module is formatted, how its command line arguments are used, how docstrings work and connect to the python help system, how the testing functions work, and how to load the code and use it in the notebook. All these things you should understand by now, so it's a good check that you are following everything. Verify that running `nosetests3` in a terminal runs the tests and produces output you expect.
2. Complete the `numpy` array implementation of the Gaussian function in the module and verify that its tests work. Plot the function in the notebook to verify it reproduces the results of the list implementation. Benchmark the performance in the notebook and compare it to the performance of the reference list implementation. 
3. Create both list and array implementations of the "sinc" function: $$ \text{sinc}(x) = \frac{\sin(x)}{x}.$$ Follow the style of the Gaussian function implementations for reference. Plot and benchmark the implementations in the notebook. Comment on how many points are needed per period of the "sinc" to obtain an accurate plot. 
4. Create both list and array implementations of a frequency-chirped sine wave: $$\text{sinf}(x) = \sin\left(\frac{1}{x}\right).$$ What difficulties are there in implementing this function? Comment on the how many points per period will be necessary to obtain an accurate plot.



