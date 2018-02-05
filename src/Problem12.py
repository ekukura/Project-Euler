#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:35:15 2017

@author: emilykukura

What is the value of the first triangle number to have over 
five hundred divisors?

"""

import math, time

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
        else:    
            order = get_order(remaining_num, next_factor)
            my_factors[next_factor] = order
            remaining_num = int(remaining_num / math.pow(next_factor,order))
        
    return my_factors

#Let the prime factorization of n be:
#n = p_1^a_1 * p_2^a_2 * ... * p_k^a_k
#Then the below is a result of the bijection between the set 
#of factors of n and the set of ordered pairs
#(b_1, b_2, ..., b_k) s.t. 0 <= b_i <= a_i for 1 <= i <= k
#Since there are (a_1+1)*(a_2+1)*...*(a_k+1) such 
#ordered pairs, there are also this many factors
def get_num_factors(n):
    factors = factor(n)
    #print(factors)
    my_list = [factors[i] + 1 for i in factors]
    #print(my_list)
    
    prod = 1
    for i in range(len(my_list)):
        prod *= my_list[i]
        
    return prod


if __name__ == '__main__':

    print(factor(500))
    print(math.pow(2,4)*math.pow(3,4)*math.pow(5,4)*7*11)   
    print(math.pow(2,4)*math.pow(3,4)*math.pow(5,2)*7*11*13)
    print(get_num_factors(math.pow(2,4)*math.pow(3,4)*math.pow(5,2)*7*11*13))

    #note 500 = 2^2*5^3 = 2*2*5*5*5 
    #thus smallest # with EXACTLY 500 factors 
    #is 2^4*3^4*5^4*7*11 = 62,370,000 (see explanation of 
    #get_num_factors method
    
    #(smallest # with at least 500 could be higher...)
    #In fact,
    #note 2*2*5*5*5 < 2*2*5*5*(2*3)
    #Thus 2*2*5*5*(2*3) has > 500 factors, and since 13 < 5^2 we can get 
    #an even smaller # with >= 500 factors by taking 
    #2^4*3^4*5^2*7*11*13 = 32,432,400
    #Now, since 17 > 3^2 we stop here, and this is the smallest # with
    #at least 500 factors
    #could write an algorithm for determining smallest number 
    #with at least m factors based off of this logic...

    
    #Let t = triangle(m) be the number we are searching for (the 
    #first triangle number to have over five hundred divisors)
    #then since 32,432,400 is the smallest number with at 
    #least 500 factors:
    #32,432,400 <= t = triangle(m) = m*(m+1)/2 <= (m+1)^2/2.
    #So, sqrt(2*32,432,400) <= m, and since m is an integer,
    # ceil(sqrt(2*32,432,400)) <= m. Thus we can 
    # start our search with num = ceil(sqrt(2*32,432,400)
    
    start = time.time()
    min_num_divisors = 500
    smallest_num_g500_divisors = math.pow(2,4)*math.pow(3,4)*math.pow(5,2)*7*11*13
    start_num = math.ceil(math.sqrt(2*smallest_num_g500_divisors))
    print("Starting with number", start_num,"\n")

    num = start_num
    tri_num = triangle2(num)
    num_factors = get_num_factors(tri_num)
    
    while num_factors <= min_num_divisors:
        num += 1
        tri_num = triangle2(num)
        num_factors = get_num_factors(tri_num)
        #print(num, tri_num, num_factors)
      
    end = time.time()
      
    print("result is:", tri_num)
    print("took {} seconds".format(end-start))


