#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:10:41 2017

@author: emilykukura
"""

#What is the largest prime factor 
#of the number 600851475143 ?

import math
import time


#returns (True, 1) if no prime factors, and (False, largestFactor) otherwise
def isPrime(x):
    determinedComp = False
    max_i = math.floor(math.sqrt(x))
    i = 2
    largestFactor = 1 
    while i <= max_i and not determinedComp:
        if x % i == 0: #then x has a factor
            determinedComp = True
            largestFactor = x / i
        i += 1
    return(not determinedComp, round(largestFactor))
    #return(not determinedComp)

#testing
#print(isPrime(24)[1])
#print(isPrime(17)[0])

def largestPrimeFactor(x):
    res = isPrime(x)
    if res[0]: #so x is prime
        return x
    else: #so x is composite
        a = res[1]
        b = round(x / res[1])
        return(max(largestPrimeFactor(a), largestPrimeFactor(b)))

if __name__ == '__main__':
    start = time.time()
    x = 600851475143 
    print("The largest prime factor of",x, "is", largestPrimeFactor(x))
    print("Computed in:", time.time()-start)
    #number x
    #if x prime, done
    #else
        #x = a * b
        #res = max(largestPrimeFactor(a), largestPrimeFactor(b))
    
