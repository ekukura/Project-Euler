#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:29:54 2017

@author: emilykukura
"""
import time
import math
import numpy as np
import statistics as stats
#What is the smallest positive number that is 
#evenly divisible by all of the numbers from 1 to 20?
#e.g. 2520 is the smallest number that 
#can be divided by each of the numbers from 1 to 10 without any remainder.

#i.e. what is lcm(1,2,...,20)
#note lcm(a,b,c) = lcm(lcm(a,b),c)
def gcd(a,b): 
    l = max(a,b) #l = larger
    s = min(a,b) #s = smaller
    GCD = 0
    #implement Euclidean algorithm here
    if l == 0:
        GCD = s
    elif s == 0:
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
        list_minus_first = alist[1:]
        return lcm(alist[0], lcmList(list_minus_first))


start = time.time()
max_num = 10

""" 
#Solution 1 

myList = [i for i in range(1,max_num+1)]
res = lcmList(myList)
#"""
#res = 232792560


#"""
#Solution 2
primes = [2,3,5,7,11,13,17, 19, 21,23,29,31, 37, 41, 43, 47, 53, 59, 
          61, 67, 71, 73, 79, 83, 89, 97, 101]
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
        #if p^a <= max_num
        # alog(p) = log(p^a) <= log(max_num)
        # a <= log(max_num-p)
        #max_a = floor(log(max_num-p))
res = 1
for i in range(max_index + 1):
    res *= pow(primes[i],  max_prime_power[i])
#"""

time_taken = time.time()-start
#timesList[i] = time.time()-start

print("Result is:", res, "and average time was: ", time_taken)
#print("Result is:", res, "and average time was: ", stats.mean(timesList))
           
#testing  
#print(gcd(6,8))  
    

#only need primes < max_num
'''
def get_max_index(num, aList):
    #returns result of max
    
max_index = get_max_index(max_num, primes)
'''
