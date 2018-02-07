#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:37:24 2017

@author: emilykukura

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import math, time


def isPrime(x):
    foundComposite = False
    if x == 2:
        return True
    elif  x % 2 == 0:
        return False
    else:   
        i = 3
        while i <= math.floor(math.sqrt(x)) and not foundComposite:
            #testing all possible lower divisors
            if x % i == 0:
                foundComposite = True
            i += 2
        return not foundComposite

def solution_1(primeIndex):
#### Solution 1, plain brute force #######
    counter = 2

    #all primes greater than 2 are odd
    i = 3
    while counter < primeIndex:
        i+=2
        if isPrime(i):
            counter += 1
            
    return i

def solution_2(primeIndex):
###### Solution 2, modified brute force ########

    #does from primeIndex > 2 (1st two primes are 2,3)
    counter = 2
    i = 3
    while counter < primeIndex:
        i+=2 #don't need to test even numbers past 2 
        if i % 3 == 0:
            pass
        elif i > 5 and i % 5 == 0:
            pass
        elif i > 7 and i % 7 == 0:
            pass
        elif i > 11 and i % 11 == 0:
            pass
        elif isPrime(i):
            counter += 1

    return i


if __name__ == '__main__':  
    
    start = time.time()
    res_1 = solution_1(10001)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))  
    
    start = time.time()
    res_2 = solution_2(10001)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))  
    
    #Answer: 104743
   
 

