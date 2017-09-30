# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:52:28 2017

@author: Zana Daniel
"""

# [THIS WILL MAKE OR BREAK YOUR FUNCTION] the lru_cache package caches(saves) each n calculation so that the function doesn't have to re-calculate n on every sequence and ultimately slow down to a fatal point
from functools import lru_cache

# maxsize means we're saving the up to 1000 values of n
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# prints only the n-th term
def print_n(n):
    print("\nn=" + str(n) + ":", fibonacci(n))

# prints the n-th term and all the previous terms leading up to it
def print_n_all(n):
    for n in range(1, n+1):
        print("n=" + str(n) + ":", fibonacci(n))

print_n_all(11)
print_n(11)
