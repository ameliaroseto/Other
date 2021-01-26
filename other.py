#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np

def gen_gaussian_list(a, b, n=1000):

    dx = (b-a)/(n-1)                         # spacing between points
    x = [a + k*dx for k in range(n)]         # domain list
    
    # Local implementation of a Gaussian function
    def gauss(x):
        return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
    
    g = [gauss(xk) for xk in x]                  # range list
    return (x, g)


def gen_gaussian_array(a, b, n=1000):

    x = np.linspace(a, b, endpoint=True, num=n)

    def gauss(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)

    g = gauss(x)
    return (x, g)

def sinc_list(a, b, n=1000):
  
    dx = (b-a)/(n-1)                         # spacing between points
    x = [a + k*dx for k in range(n)]         # domain list
    x.remove(0)

    def sinc(x):
        return ((math.sin(x)/x))
    s = [sinc(xk) for xk in x]
    return (x,s)

def sinc_array(a, b, n=1000):

    x = np.linspace(a, b, endpoint=True, num=n)

    def sinc(x):
        ones = np.ones_like(x)
        return(np.divide(np.sin(x), x, out = ones, where=x!=0))

    s = sinc(x)
    return (x, s)

def sinf_list(a, b, n=1000):
    
    x = np.linspace(a, b, endpoint=True, num=n)

    def sinf(x):
        ones = np.ones_like(x)
        return(np.sin(np.divide(1, x, out = ones, where=x!=0)))

    s = sinf(x)
    return (x, s)

def main(a,b,n=1000):

    x, g = gen_gaussian_list(a,b,n)
    for (xk, gk) in zip(x, g):
        print("({}, {})".format(xk, gk))


# Protected main block for command line operation
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        n = int(sys.argv[3])
        main(a,b,n)
    elif len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        main(a,b)
    else:
        print("Usage: cw07.py a b [n]")
        print("  a : float, lower bound of domain")
        print("  b : float, upper bound of domain")
        print("  n : integer, number of points in domain")
        exit(1)

