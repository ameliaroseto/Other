[![Build Status](https://travis-ci.com/chapman-phys220-2018f/cw07-late_for_class.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/cw07-late_for_class)

**Author(s):** **Amelia Roseto**

## Specification

1. Go through the [Numpy/Pandas Slides](http://slides.com/profdressel/numpy-and-pandas-overview/) that introduce the `numpy` and `pandas` libraries and how to use them. Add to the Jupyter notebook `CW07.ipynb` in the current repository to test bits of code as you read through slides to make sure you understand. The rest of the notebook displays useful examples that should help orient you with the new concepts.
1. With your partner, go through the python code in the repository showing the reference list implementation of the Gaussian function: $$g(x) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{x^2}{2} \right).$$ Make sure you observe how the python module is formatted, how its command line arguments are used, how docstrings work and connect to the python help system, how the testing functions work, and how to load the code and use it in the notebook. All these things you should understand by now, so it's a good check that you are following everything. Verify that running `nosetests3` in a terminal runs the tests and produces output you expect.
1. Complete the `numpy` array implementation of the Gaussian function in the module and verify that its tests work. Plot the function in the notebook to verify it reproduces the results of the list implementation. Benchmark the performance in the notebook and compare it to the performance of the reference list implementation. (Hint: Use array vectorization, meaning avoid all explicit for loops in favor of functions inside `numpy` that automatically distribute (map over) arrays. You may find the [numpy Documentation](https://docs.scipy.org/doc/numpy/reference/index.html) useful to browse while coding - it is common for coders to keep a window open with relevant library documentation for reference.)
1. Create both list and array implementations of the "sinc" function: $$ \text{sinc}(x) = \frac{\sin(x)}{x}.$$ Follow the style of the Gaussian function implementations for reference. Plot and benchmark the implementations in the notebook. Comment on how many points are needed per period of the "sinc" to obtain an accurate plot. (Hint: in the division you will need to skip the single point $x=0$. The `where` and `out` keyword arguments of `numpy.divide` may be useful here.)
1. Create both list and array implementations of a frequency-chirped sine wave: $$\text{sinf}(x) = \sin\left(\frac{1}{x}\right).$$ What difficulties are there in implementing this function? Comment on the how many points per period will be necessary to obtain an accurate plot.


Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.


