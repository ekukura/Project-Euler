#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:18:26 2017

@author: emilykukura

Find the sum of the primes smaller than 2 million.

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
    
# determine_primes2 SLOWER than determine_primes1
# Both the Sieve of Eratosthenes
def determine_primes2(max_x):
    
    if max_x < 2:
        return "no primes"
    elif max_x == 2:
        return [2]
    
    max_divisor = math.floor(math.sqrt(max_x))
    
    #pps are all possible primes
    pps = [2]
    pps.extend([2*j+1 for j in range(1, math.floor((max_x+1)/2))])
    prime_index = 1
    cur_poss_prime = pps[prime_index]


    while cur_poss_prime <= max_divisor:
        print(cur_poss_prime)
        #print(cur_poss_prime)
        #remove all possible multiples       
        max_k = math.floor(max_x / cur_poss_prime)

        for k in range(2, max_k + 1):
            try:
                pps.remove(k*cur_poss_prime)
            except:
                pass
        
        #print(pps)
        prime_index += 1
        cur_poss_prime = pps[prime_index]
       
    return pps
    

# determines all prime numbers <= max_x
def determine_primes(max_x):
    
    if max_x < 2:
        return "no primes"
    elif max_x == 2:
        return [2]
    
    max_divisor = math.floor(math.sqrt(max_x))
    
    #pps = [j for j in range(2, max_x+1)]
    pps = {2}
    pps = set.union(pps, {2*j+1 for j in range(1, math.floor((max_x+1)/2))})
    
    found_primes = set()
    cur_prime = min(pps)  

    while cur_prime <= max_divisor:
        
        found_primes = set.union(found_primes, {cur_prime})

        #remove all possible multiples       
        max_k = math.floor(max_x / cur_prime)
        multiples = {k*cur_prime for k in range(cur_prime, max_k+1)}
        pps = pps - multiples
      
        cur_prime = min(pps - found_primes)
       
    return pps
    
    
def sum_primes(max_x):
    p_sum = 0
    for i in range(2, max_x):
        if isPrime(i):
            p_sum += i
            
    return p_sum

if __name__ == '__main__':
 
    max_num = 2000000
    
    start = time.time() 
    primes = determine_primes(max_num)
    #print(primes)
    res_1 = sum(primes)
    print("sum is:", res_1)
    print("Took:", round(time.time() - start, 6), "seconds")
    
    ''' Don't do this one for max_num >= 200,000 (at 200,000, takes ~4.16 s)
    start = time.time() 
    res_2 = sum_primes(max_num)
    print("sum is:", res_2)
    print("Took:", round(time.time() - start, 6), "seconds")
    #'''
    
    #Took: 9.498652 seconds
    #Answer: 142913828922




