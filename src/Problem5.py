#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:29:54 2017

@author: emilykukura
"""
import time, math
import numpy as np
import statistics as stats

'''
What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20?
e.g. 2520 is the smallest number that 
can be divided by each of the numbers from 1 to 10 
without any remainder.
'''

#i.e. what is lcm(1,2,...,20)
#note lcm(a,b,c) = lcm(lcm(a,b),c)
#assumes a,b non-negative
def gcd(a,b): 
    l = max(a,b) #l = larger
    s = min(a,b) #s = smaller
    GCD = 0
    #implement Euclidean algorithm here
    if s == 0:
        GCD = l
    else:
        r = l % s
        GCD = gcd(s,r)
        
    return GCD

def lcm(a,b):
    return a*b/gcd(a,b)

def lcmList(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return lcm(alist[0], lcmList(alist[1:]))

def solution_1(max_num):
    
    myList = [i for i in range(1,max_num+1)]
    res = lcmList(myList)
    
    return res

def solution_2(max_num):

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31, 37, 41, 
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    max_prime_power = [0] * len(primes)
    #only need primes < max_num
    toContinue = True
    i = 0
    max_index = 0
    while toContinue:
        curPrime = primes[i]
        if curPrime > max_num:
            max_index = i-1
            toContinue = False
        else:
            #find max power of prime <= max_num
            max_prime_power[i] = math.floor(math.log(max_num)/ math.log(curPrime))
            i += 1
            #In prime factorization of i = 1...max_num, for each i 
            #must have p^a <= i for each prime p, and so 
            #in particular p^a <= max_num for each prime p. Thus:
            # alog(p) = log(p^a) <= log(max_num)
            # a <= log(max_num-p)
            #So max_a = floor(log(max_num-p))
            #further, since p^max_a <= max_num, p^max_a = i for some i in [1,max_num]
            #and so in the prime factorization of lcm(1...max_num), the 
            #exponent of p is AT LEAST max_a. Thus the 
            #exponent of p is exactly max_a
            
    res = 1
    for i in range(max_index + 1):
        res *= pow(primes[i],  max_prime_power[i])
    
    #print(primes)
    #print(max_prime_power)
    return res


if __name__ == '__main__':

    #start = time.time()
    #res1 = solution_1(10)
    #end = time.time()
    #print("res = {}\nTook {} seconds".format(res1, end-start))
    #2520 should be answer for test case max_num = 10
    print(gcd(6,8))  
    
    start = time.time()
    res_1 = solution_1(20)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))    
    
    start = time.time()
    res_2 = solution_2(20)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))    
    #Answer: 232792560

