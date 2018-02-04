#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:35:15 2017

@author: emilykukura

What is the value of the first triangle number to have over five hundred divisors?

"""

import math

def triangle(n):
    if n == 1:
        return 1
    else:
        return triangle(n-1) + n

def triangle2(n):
    return int(n*(n+1)/2)

def getSmallestNonOneFactor(k):
    if k == 1:
        return -1
    
    max_min_divisor = int(math.floor(math.sqrt(k)))
    #print(max_min_divisor)
    p = 2
    divisorFound = False
    
    while not divisorFound and p <= max_min_divisor:
        if k % p == 0:
            divisorFound = True
        elif p == 2:
            p += 1
        else:
            p += 2
    
    if divisorFound:
        return p
    else:
        return k

def isPrime(k):
    max_min_divisor = int(math.floor(math.sqrt(k)))
    #print(max_min_divisor)
    p = 2
    divisorFound = False
    
    while not divisorFound and p <= max_min_divisor:
        if k % p == 0:
            divisorFound = True
        elif p == 2:
            p += 1
        else:
            p += 2
    
    return not divisorFound

#my_dict = {1:2, 3:4}
#my_dict[5] = 6

def get_order(k, prime_divisor):
    order = 1
    divides = True
    while divides and order < k:
        if (k % int(math.pow(prime_divisor, order+1)) == 0):
            order += 1
        else:
            divides = False
            
    return order
    
    
def factor(k):
    factors_remain = True    
    remaining_num = k
    my_factors = {}
    
    while factors_remain:
        next_factor = getSmallestNonOneFactor(remaining_num)
        if next_factor == -1: #this means remaining num is 1
            factors_remain = False
        elif next_factor == remaining_num: #this means remaining_num is prime
            my_factors[next_factor] = 1
            factors_remain = False          
        else:    
            order = get_order(remaining_num, next_factor)
            my_factors[next_factor] = order
            remaining_num = int(remaining_num / math.pow(next_factor,order))
        
    return my_factors


def get_num_factors(n):
    factors = factor(n)
    print(factors)
    
    my_list = [factors[i] + 1 for i in factors]
    print(my_list)
    
    prod = 1
    for i in range(len(my_list)):
        prod *= my_list[i]
        
    print(prod)
    return prod


'''
min_num_divisors = 500
num = 2079
tri_num = triangle2(num)
num_factors = get_num_factors(tri_num)

while num_factors <= min_num_divisors:
    num += 1
    tri_num = triangle2(num)
    num_factors = get_num_factors(tri_num)
    print(num, tri_num, num_factors)
    
print("result is:", tri_num)
'''


#print(getSmallestNonOneFactor(71))
#comments


'''

nope, this is just one factorization
def two_factor(k):
    max_min_divisor = int(math.floor(math.sqrt(k)))
    #print(max_min_divisor)
    p = max_min_divisor
    divisorFound = False
    
    small_divisor = 1
    large_divisor = k
            
    while not divisorFound and p >= 1:
        if k % p == 0:
            divisorFound = True
            small_divisor = p
            large_divisor = int(k / p)
        else:
            p -= 1
    
    return small_divisor, large_divisor


def get_divisors(k):
    
    a, b = two_factor(k)
    if a == 1: #this means k is prime
        return {1, k}   
    else:
        return set.union(set.union({k},get_divisors(a)), get_divisors(b))
    #factor as k = a * b
    #then divisors(k) = divisors(a) union divisors(b)
    
    
#this is real messed up
def num_factors(k):
    num_factors = 2 #1,k always divisors
    reduced = False
    smallest_Divisor = getSmallestNonTrivialFactor(k)
    remaining_num = k
    if smallest_Divisor == -1:
        reduced = True
    
    while not reduced:
        largest_Divisor = remaining_num/smallest_Divisor
        num_divisors += 2
        
        remaining_num /= (smallest_Divisor*largest_Divisor)
        smallest_Divisor = getSmallestNonTrivialFactor(remaining_num)
        if smallest_Divisor == -1:
            reduced = True
            
    return num_factors

for m in range(4,12):
    print(m, num_divisors(m))

for m in range(10):
    print(m, getSmallestNonTrivialFactor(m))
#'''        