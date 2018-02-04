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
            i += 1
        return not foundComposite

start = time.time()

#### Solution 1, plain brute force #######
#"""
counter = 2
primeIndex = 10001
#while counter <= primeIndex :
'''
i = 2
while True:
    if isPrime(i):
        counter += 1
    if counter == primeIndex:
        break
    i += 1
'''
#all primes greater than 2 are odd
i = 3
while counter < primeIndex:
    i+=2
    if isPrime(i):
        counter += 1
        
print(i)

#10001st prime:
#104743
#In time: 1.3114359378814697 seconds
#"""

###### Solution 2, modified brute force ########
"""
primeIndex = 25
'''
#does from primeIndex > 1 (1st prime is 2)
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
'''
      
#does from primeIndex > 5 (6th prime is 13)
counter = 6
i = 13
while counter < primeIndex:
    i+=2 #don't need to test even numbers past 2 
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0 or i % 13 == 0:
        pass
    else:
        print(i)
        if isPrime(i):
            counter += 1
#"""        
print(time.time()-start)
    
'''
print(7, isPrime(7))
print(8, isPrime(8))
print(51, isPrime(51))
print(31, isPrime(31))
#'''               
