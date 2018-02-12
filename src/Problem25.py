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

import time, math


def rec_fib(m):
    if m == 1:
        return 1
    elif m == 2:
        return 1
    else:
        return rec_fib(m-1)+rec_fib(m-2)
    
def dyn_fib(m):
    d = {1:1, 2:1}
    if m > 2:
        for i in range(3, m+1):
            d[i] = d[i-1] + d[i-2]
    return d[m]

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


#fibCalculator is some method which maps n->fibonacci(n) 
#This uses a bisecting search over the indices
def bisection_search(n, fibCalculator, d = None):
    ind = 0
    lower_ind = 0
    upper_ind = None
    #divide and conquer approach
    found = False
    while not found: #need max_len = n
        if upper_ind == None: #increment until can find upper bound
            ind += int(math.floor(n/2))
        else:
            ind = lower_ind + int(math.floor((upper_ind - lower_ind)/2)) #look halfway between uper and lower bound
         
        #print("calculating ind = {}".format(ind)) 
        if d:
            res, d = fibCalculator(ind, d)  
        else:
            res = fibCalculator(ind)
            
        cur_len = len(str(res))

        if cur_len < n:
            if upper_ind: #if here, HAVE found a fib. # w/ len >= n
                if upper_ind - lower_ind == 1: #if here, then done since upper_ind must be smallest ind s.t. len(fib(ind)) = n
                    found = True
                    ind = upper_ind
                else:
                    lower_ind = ind
            else:
                lower_ind = ind
                
        else: #cur_len >= n
            if upper_ind:
                if upper_ind - lower_ind == 1:
                    found = True
                else:
                    upper_ind = ind
            else:
                upper_ind = ind
        
        #print("ind = {}, cur_len = {}\nlower_ind = {}, upper_ind = {}".format(
        #            ind, cur_len, lower_ind, upper_ind))
        
    return ind

#fibCalculator is some method which maps n->fibonacci(n) 
#this uses a simple incrementing search over the indices
def increment_search(n, fibCalculator, d = None):
    ind = 0
    max_len = 0
    while max_len < n:
        ind += 1

        if d:
            res, d = fibCalculator(ind, d)  
        else:
            res = fibCalculator(ind)

        max_len = len(str(res))
        #print(ind, max_len)
        
    return ind



def solution_1(n):
    return increment_search(n, rec_fib)

def solution_2(n):
    return increment_search(n, dyn_fib)

def solution_3(n):
    return bisection_search(n, rec_fib)

def solution_4(n):
    return bisection_search(n, dyn_fib)

def solution_5(n):
    d = {1:1, 2:1}   
    return increment_search(n, dyn_fib2, d)

#below is best solution, uses dictionary and bisection
def solution_6(n):
    d = {1:1, 2:1}   
    return bisection_search(n, dyn_fib2, d)

if __name__ == '__main__':
    
    #num = 10
    num = 1000 
    
    # The recursive Solutions 1 and 3 are SLOW. Remainder of solutiosn are
    # dynamic and are WAY getter
    
    '''Shouldn't do this one for num > 8 (at num = 8 takes ~16.1 s)
    start = time.time()
    res1 = solution_1(num)
    end = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res1, end-start))
    #'''

    '''Shouldn't do this one for num > 1000 (at num = 1000 takes ~4.25 s)
    start = time.time()
    res2 = solution_2(num)
    end = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res2, end-start))
    #'''
    
    '''Shouldn't do this one for num > 8 (at num = 8 takes ~15.6 s)
    start = time.time()
    res3 = solution_3(num)
    end = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res3, end-start))
    #'''
    
    #'''Shouldn't do for num > 20,000 (at num = 20000 took ~8.54 seconds)
    start = time.time()
    res4 = solution_4(num)
    end = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res4, end-start))
    #'''

    #'''Shouldn't do for num > 4,000 (at num = 4,000 took ~5.87 seconds)
    start = time.time()
    res5 = solution_5(num)
    end = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res5, end-start))
    #'''
    
    #Shouldn't do for num > 40,000 (at num = 40,000 took ~4.42 seconds)
    start = time.time()
    res6 = solution_6(num)
    end = time.time()
    print("\nres = {}. Took {} seconds.\n".format(res6, end-start))

    #could try another solution which combines benefits of solutions 4 and 5
    
    # Answer: 4782
    