#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:53:56 2017

@author: emilykukura

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b 
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math, time

def get_divisor_exponent(num, divisor):

    cur_exp = 0
    while num % divisor == 0:
        cur_exp += 1
        num = int (num / divisor)
    
    return cur_exp
    
    
def getSmallestNonOneFactor(k):
    if k == 1:
        return -1
    
    max_min_divisor = int(math.floor(math.sqrt(k)))
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
        return k #if no divisor found, then k is prime so its only factors are 1 and k
    
    
def factor(k):
    factors_remain = True    
    remaining_num = k
    my_factors = {} #dictionary which contains the prime factors of k along with their orders
    #in the prime factorization of k
    
    while factors_remain:
        next_factor = getSmallestNonOneFactor(remaining_num)
        if next_factor == -1: #this means remaining num is 1
            factors_remain = False
        elif next_factor == remaining_num: #this means remaining_num is prime
            my_factors[next_factor] = 1
            factors_remain = False          
        else:    
            order = get_divisor_exponent(remaining_num, next_factor)
            my_factors[next_factor] = order
            remaining_num = int(remaining_num / math.pow(next_factor,order))
        
    return my_factors


def get_all_divisors(factor_dict):
    cur_factor, cur_exponent = factor_dict.popitem()
    
    if len(factor_dict) == 0:
        divisor_set = {int(math.pow(cur_factor, power)) for power in range(cur_exponent + 1)}
            
    else:
        remaining_divisors = get_all_divisors(factor_dict)
        
        divisor_set = set(remaining_divisors) #divisor_set is a new copy of remaining_divisors set
        for power in range(1, cur_exponent + 1):
            multiplier = int(pow(cur_factor, power))
            mult_set = {multiplier * el for el in remaining_divisors}
            divisor_set = set.union(divisor_set, mult_set)
        
    return divisor_set


def d(n): #finds sum of proper divisors of n
    #factorize n, then take all possible combinations 
    prime_factors = factor(n)
    divisor_set = get_all_divisors(prime_factors)
    divisor_set.remove(n)
            
    return sum(divisor_set)

 
# returns set of amicable numbers <= L
# note if (a,b) amicable pair, then (a,c) and (c,b) NOT amicable for any c (c != a,b)
# since d(a) = b and d(b) = a. Thus if b is an amicable mate to a, then we can remove b 
# from further consideration as a mate of any other number 
def amicable_numbers(L):
    #for a=2:L
    #find d(a) = n and try d(n). If n hasn't already been eliminated from eligible 
    #amicable numbers, compute d(n) and if d(n) = a, add a and n to amicable pairs; 
    #remove n from set to try; increment a
    candidates = {i for i in range(2,L+1)}
    amicable_numbers = set()
    
    while len(candidates) > 0:
        cur_candidate = candidates.pop()
        cur_eligible_mate = d(cur_candidate)
        if cur_eligible_mate in candidates and cur_candidate == d(cur_eligible_mate):
            amicable_numbers = set.union(amicable_numbers, {cur_candidate, cur_eligible_mate})
            candidates.remove(cur_eligible_mate)          

    return amicable_numbers


def solution_1(num):
    am_nums = amicable_numbers(num)
    res = sum(am_nums)
    return res, am_nums

if __name__ == '__main__':
    
    num = 10000
    
    start = time.time()
    res, am_nums = solution_1(num)
    end = time.time()   
    print("The amicable numbers under {} are \n{}.\nTheir sum is {}\n".format(num, am_nums, res))
    print("Took {} seconds".format(end-start))
    
    # Answer: 31626
    
    '''
    print(d(220))
    print(d(284))
    
    n = 220
    prime_factors = factor(n)
    print("\nThe prime factors of {} are:\n{}\n".format(n, prime_factors))
    divisor_set = get_all_divisors(prime_factors)
    print("The divisors of {} are:\n{}\n".format(n, sorted(divisor_set)))
    res = sum(divisor_set) - n
    print("res = ", res)
    
    m = 284
    #prime_factors = get_prime_factors(m)
    prime_factors = factor(m)
    print("\nThe prime factors of {} are:\n{}\n".format(m, prime_factors))
    divisor_set = get_all_divisors(prime_factors)
    print("The divisors of {} are:\n{}\n".format(m, sorted(divisor_set)))
    res = sum(divisor_set) - m
    print("res = ", res)
    
    #'''
    
