#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:34:12 2017

@author: emilykukura

Euler discovered the remarkable quadratic formula: n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive 
integer values 0≤n≤39. However, when n=40,
40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,
41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes 
for the consecutive values 0≤n≤79. The product of the coefficients, 
−79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n, e.g. |11|=11 and |−4|=4. Find the 
product of the coefficients, a and b, for the quadratic expression that produces 
the maximum number of primes for consecutive values of n, starting with n=0.

"""

import math, time
import numpy as np

def get_smallest_non1_divisor(num, start_p):
    if num == 1:
        res = None
    elif start_p > num:
        res = None   
    else:
        max_min_divisor = int(math.floor(math.sqrt(num)))
        divisor_found = False
        p = 2
        while p <= max_min_divisor and not divisor_found:
            if num % p == 0:
                divisor_found = True
                res = p
            else:
                if p == 2:
                    p += 1
                else:
                    p += 2
        
        if not divisor_found: #in this case must be prime number
            res = num
        
    return res
    
def isPrime(num):
    if num <= 1:
        res = False 
    else:
        divisor_found = False
        max_min_divisor = int(math.floor(math.sqrt(num)))
        d = 2
        while not divisor_found and d <= max_min_divisor:
            if num % d == 0:
                divisor_found = True
            else:
                if d == 2:
                    d += 1
                else:
                    d += 2
        
        res = not divisor_found                
        
    return res

def get_number_consecutive_primes(a,b):
    #n^2 + a * n + b
    composite_found = False
    n = 0
    while not composite_found:
        cur_cand = pow(n,2) + a * n + b
        if isPrime(cur_cand):
            n += 1
        else:
            composite_found = True            
            
    return n

#note, even b always divisible at n = 2, so skip
def get_max_prod(max_a_mod, max_b_mod):
    
    my_max = 0
    my_prod = 0
    a_max = None
    b_max = None
    if max_b_mod % 2 == 0: 
        max_b_mod -= 1

    
    for a in range(-max_a_mod, max_a_mod + 1):
        for b in np.arange(-max_b_mod, max_b_mod + 1, 2):
           cur_max = get_number_consecutive_primes(a,b)
           if cur_max > my_max:
               a_max = a
               b_max = b
               my_max = cur_max
               my_prod = a * b;
    
    return a_max, b_max, my_max, my_prod

#returns largest b value in candidates which does NOT have divisor smaller 
#than cur_max, and the remaining candidates
#or None, {} if none such
def get_next_b_val(max_b_modulus, candidates, cur_max):
    '''
    print("initial inputs:")
    print(max_b_modulus)
    print(candidates)
    print(cur_max)
    print()
    '''
    next_b_found = False
    next_b = None
    while len(candidates) > 0 and not candidates == {1} and not next_b_found:
        
        b = max(candidates)
        #print("\nb = ", b)
        if b < cur_max: #if reach this state, then there is NO viable b
            candidates = set() 
            
        s = get_smallest_non1_divisor(b,2)
        #print("s = ", s)
        if s < cur_max: #if s < cur_max, remove s and all its multiples in remaining set
            candidates = candidates - get_multiples(s, max_b_modulus)  
            #candidates = candidates - {b} #for good measure--in reality should be accounted for in line above                  
        else:
            #print("smallest divisor = ", s)
            next_b_found = True
            next_b = b           
        #print("candidates:\n", candidates)
        
    return next_b, candidates
    

def get_multiples(m, max_val):
    max_multiplier = int(math.floor(max_val/m))
    return {m*k for k in range(1, max_multiplier+1)}

def get_optimized_max_prod(max_a_mod, max_b_mod):
    
    my_max = 0
    my_prod = 0
    a_max = None
    b_max = None
    if max_b_mod % 2 == 0: 
        max_b_mod -= 1
        
    cand_b_abs = {i for i in np.arange(1, max_b_mod + 1, 2)}
    
    #stop = False
    b = max(cand_b_abs) #check both + and - of b
    #done once b <= my_max, as then at most b'< b <= my_max consec. primes for all remaining b candidates
    while not b == None and b > my_max and len(cand_b_abs) > 0: #and not stop:
        #print("b = ", b)
        for a in range(-max_a_mod, max_a_mod + 1):
           #n_iters = 0
           cur_max_pos = get_number_consecutive_primes(a,b)
           cur_max_neg = get_number_consecutive_primes(a,-b)
           #print("a = ", a)
           #print(cur_max_pos)
           #print(cur_max_neg)
           
           if max(cur_max_pos, cur_max_neg) > my_max:  
               if cur_max_pos > my_max:
                   a_max = a
                   b_max = b
                   my_max = cur_max_pos
                   my_prod = a * b
                   
               if cur_max_neg > my_max:
                   a_max = a
                   b_max = b
                   my_max = cur_max_neg
                   my_prod = a * b    
                   
        cand_b_abs = cand_b_abs - {b}
        #print(cand_b_abs)       
        #print("my_max = ", my_max)
           
        #to make even faster, remove multiples of ANY divisor < my_max,
        #not JUST the smallest one
        b, cand_b_abs = get_next_b_val(max_b_mod, set(cand_b_abs), my_max)
           
    return a_max, b_max, my_max, my_prod


max_a_val = 999
max_b_val = 1000
start = time.time()
res = get_max_prod(max_a_val, max_b_val)
end = time.time()
print("The resulting tuple is (a_max, b_max, my_max, my_prod) = {}.\n"
      "Took {} seconds".format(res, end-start))
start2 = time.time()
res2 = get_optimized_max_prod(max_a_val, max_b_val)
end2 = time.time()
print("The resulting tuple is (a_max, b_max, my_max, my_prod) = {}.\n"
      "Took {} seconds".format(res2, end2-start2))

print()

'''
rs = {1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
mm =  48
r, cands = get_next_b_val(100, rs, mm)
print("\nr = ", r)
print("\ncands = ", cands)
'''

'''
m = 200
cand_b_abs = {i for i in np.arange(1, m + 1, 2)}
print(cand_b_abs)
b = min(cand_b_abs)

stop = False
while b <= m + 1 and len(cand_b_abs) > 0:
    print("b = {}\n".format(b))
    if b == 1:
       cand_b_abs = cand_b_abs - {1}
    else:
       multiples = get_multiples(b, m) 
       print("multiples:{}\n".format(multiples))
       cand_b_abs = cand_b_abs - get_multiples(b, m) 
       print("cand_b_abs:\n{}\n".format(cand_b_abs))
    
    if len(cand_b_abs) > 0:
        b = min(cand_b_abs)
'''

#s = {1,3,5} - {1,2,3}
#print(s)

#for n in range(42):

#    print("For n = {}, n^2+n+41 = {}\n".format(n, pow(n,2) + n + 41))

'''

def get_optimized_max_prod2(max_a_mod, max_b_mod):
    
    my_max = 0
    my_prod = 0
    a_max = None
    b_max = None
    if max_b_mod % 2 == 0: 
        max_b_mod -= 1
        
    cand_b_abs = {i for i in np.arange(1, max_b_mod + 1, 2)}
    
    #stop = False
    b = max(cand_b_abs) #check both + and - of b
    #done once b <= my_max, as then at most b'< b <= my_max consec. primes for all remaining b candidates
    while b > my_max and b >= 1: #and not stop:
        #print("b = ", b)
        for a in range(-max_a_mod, max_a_mod + 1):
           #n_iters = 0
           cur_max_pos = get_number_consecutive_primes(a,b)
           cur_max_neg = get_number_consecutive_primes(a,-b)
           #print("a = ", a)
           #print(cur_max_pos)
           #print(cur_max_neg)
           
           if max(cur_max_pos, cur_max_neg) > my_max:  
               if cur_max_pos > my_max:
                   a_max = a
                   b_max = b
                   my_max = cur_max_pos
                   my_prod = a * b
                   
               if cur_max_neg > my_max:
                   a_max = a
                   b_max = b
                   my_max = cur_max_neg
                   my_prod = a * b    
                   
        #no matter what, remove all multiples of b
        cand_b_abs = cand_b_abs - {b}
        #print(cand_b_abs)
        if len(cand_b_abs) > 0:
            b = max(cand_b_abs)

        #print("my_max = ", my_max)
     
       #n_iters += 1
       #if n_iters == 100:
       #    print("STOP")
       #    stop = True
            
    return a_max, b_max, my_max, my_prod
    
def get_optimized_max_prod3(max_a_mod, max_b_mod):
    
    my_max = 0
    my_prod = 0
    a_max = None
    b_max = None
    if max_b_mod % 2 == 0: 
        max_b_mod -= 1
        
    #cand_a = {i for i in range(-max_a_mod, max_a_mod + 1)}
    cand_b_abs = {i for i in np.arange(1, max_b_mod + 1, 2)}
    
    #stop = False
    for a in range(-max_a_mod, max_a_mod + 1):
        cand_b_abs_for_a = set(cand_b_abs)
        b = min(cand_b_abs_for_a) #check both + and - of b
        n_iters = 0
        while b <= max_b_mod and len(cand_b_abs_for_a) > 0: #and not stop:

           cur_max_pos = get_number_consecutive_primes(a,b)
           cur_max_neg = get_number_consecutive_primes(a,-b)
           #print("a = ", a)
           #print("b = ", b)
           #print(cur_max_pos)
           #print(cur_max_neg)
           
           if max(cur_max_pos, cur_max_neg) > my_max:  
               if cur_max_pos > my_max:
                   a_max = a
                   b_max = b
                   my_max = cur_max_pos
                   my_prod = a * b
                   
               if cur_max_neg > my_max:
                   a_max = a
                   b_max = b
                   my_max = cur_max_neg
                   my_prod = a * b    
                   
           #no matter what, remove all multiples of b
           if b == 1:
               cand_b_abs_for_a = cand_b_abs_for_a - {1}
           else:
               cand_b_abs_for_a = cand_b_abs_for_a - get_multiples(b, max_b_mod)               
        
           #print(cand_b_abs_for_a)
           if len(cand_b_abs_for_a) > 0:
               b = min(cand_b_abs_for_a)
        
           #n_iters += 1
           #if n_iters == 100:
           #    print("STOP")
           #    stop = True
            
    return a_max, b_max, my_max, my_prod
'''