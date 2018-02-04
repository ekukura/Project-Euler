#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:26:51 2017

@author: emilykukura

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to 
contain 1000 digits?
"""

import time
import numpy as np


def rec_fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rec_fib(n-1)+rec_fib(n-2)
    
def dyn_fib(n):
    d = {1:1, 2:1}
    if n > 2:
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
    return d[n]

def dyn_fib2(n,d = None):
    if d == None or len(d) < 2:
        d = {1:1, 2:1}   
    max_calculated = max(d)

    if n <= max_calculated:
        return d[n], d
    else:
        for i in range(max_calculated+1, n+1):
            d[i] = d[i-1] + d[i-2]
    return d[n], d

#return the index of the first fib. number with length n
def g(n):
    d = None
    ind = 0
    max_len = 0
    while max_len < n:
        ind += 1
        #print("\nind = ", ind )
        res, d = dyn_fib2(ind, d)
        #print("res = ", res)
        max_len = len(str(res))
    
    return ind, max_len
#num = 28


#'''
num = 1000
start = time.time()
res = g(num)
end = time.time()
print("\nres = {}. Took {} seconds.\n".format(res, end-start))
#'''

"""
nums = [pow(2,i) for i in range(5,10)]
d = None
for num in nums:

    print("\nnum = ", num)  
    print("--------------")
    
    '''
    start1 = time.time()
    res1 = rec_fib(num)
    end1 = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res1, end1-start1))
    '''
    
    '''
    start2 = time.time()
    res2 = dyn_fib(num)
    end2 = time.time()
    print("res = {}.\nTook {} seconds.".format(res2, end2-start2))
    '''
    
    start3 = time.time()
    res3, d = dyn_fib2(num, d)
    end3 = time.time()
    print("res = {}.\nTook {} seconds.".format(res3, end3-start3))
    print(len(str(res3)))
    
#"""