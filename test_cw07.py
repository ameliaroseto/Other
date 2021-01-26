#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nose
import numpy as np
import cw07

def test_gauss_list():

    x,g = cw07.gen_gaussian_list(-1,1,3)
    desired = [0.24197072451914337, 0.3989422804014327, 0.24197072451914337]
    print("Obtained:",g)
    print("Desired:",desired)
    # For comparing floating point values, nose has useful helper functions
    # to ensure they are equal up to a numerical precision tolerance
    nose.tools.assert_almost_equal(g, desired)

def test_gauss_array():

    x,g = cw07.gen_gaussian_array(-1,1,3)
    desired = np.array([0.24197072451914337, 0.3989422804014327, 0.24197072451914337])
    print("Obtained:",g)
    print("Desired:",desired)
    # Numpy has built-in testing functions to iterate over arrays and compare
    # values up to certain tolerances
    np.testing.assert_almost_equal(g, desired)
