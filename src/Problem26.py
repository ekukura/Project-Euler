#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:28:28 2017

@author: emilykukura

A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen 
that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.

"""
import math, time

#####
#return prime factorization in dictionary form
def get_factorization(num):
    factorization = dict()
    cur_num = num
    min_remaining_factor_cand = 2
    while cur_num > 1 and min_remaining_factor_cand <= cur_num:
        #print("cur_num = {} and min_remaining_factor_cand = {}".format(cur_num, min_remaining_factor_cand))
        p = get_smallest_non1_divisor(cur_num, min_remaining_factor_cand)
        if p == cur_num: #so cur_num prime
            exp = 1
        else:
            exp = get_divisor_exponent(cur_num, p)
            
        factorization[p] = exp
        cur_num = int( cur_num / math.pow(p,exp) ) 
        if p == 2:
            min_remaining_factor_cand = 3
        else:
            min_remaining_factor_cand = p + 2     

    return factorization


#only defined for num >= 1, returns smallest (non-1) divisor >= start_p
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
  
    
#assumed divisor IS divisor of num
def get_divisor_exponent(num, divisor) :
    exp = 0
    cur_num = num
    while int(cur_num % divisor) == 0:
        exp += 1
        cur_num = int(cur_num / divisor)
    
    return exp


#return list of all divisors based on prime factorization
#assumed prime_factorization is a dict()
def get_divisors(prime_factorization):
    
    cur_factor, cur_exp = prime_factorization.popitem()
    #base case
    if len(prime_factorization) == 0:   
        divisor_set = {int(pow(cur_factor, exp)) for exp in range(cur_exp + 1)}
    else:
        remaining_divisors = get_divisors(prime_factorization)
        divisor_set = set(remaining_divisors)
        for divisor in remaining_divisors:
            cur_mult_set = {int(pow(cur_factor, exp) * divisor) for exp in range(1, cur_exp + 1)}
            divisor_set = set.union(divisor_set, cur_mult_set)
            
    return divisor_set

####################


#assume num <= den
def get_next_numer_and_decimal(num, den):
    #e.g. get a and m in the representation of num/den as:
    #num/den = 0.m + (num/den - 0.m) = 0.m + (num/den - m/10) 
    #= 0.m + (10*num/10*den - m*den/10*den)
    #= 0.m + ((10*num-m*den)/den)/10.
    #= 0.m + (a/den)/10
    m = math.floor(10*num/den)
    return 10 * num - m * den, m

def recip_cycle_bad(n): 
    #e.g. cycle length of 3 is 1 since 1/3 = .(3)
    # cycle length = 7 is 6 since 1/7 = 0.(142857) 
    '''
    how do I know 3 is repeating? 
    1/3 = 0.3 + (1/3 - 0.3) = 0.3 + (1/3 - 3/10) = 0.3 + (10/30 - 9/30) = 0.3 + (1/3)/10. 
    
    What about 1/7 = 0.(142857) 
    1/7 = 0.1 + (1/7 - 0.1) = 0.1 + (1/7 - 1/10) = 0.1 + (10/70 - 7/70) = 0.1 + (3/7)/10
    3/7 = 0.4 + (3/7 - 0.4) = 0.4 + (3/7 - 4/10) = 0.4 + (30/70 - 28/70) = 0.4 + (2/7)/10
    2/7 = 0.2 + (2/7 - 0.2) = 0.2 + (2/7 - 2/10) = 0.2 + (20/70 - 14/70) = 0.2 + (6/7)/10
    6/7 = 0.8 + (6/7 - 0.8) = 0.8 + (6/7 - 8/10) = 0.8 + (60/70 - 56/70) = 0.8 + (4/7)/10
    4/7 = 0.5 + (4/7 - 0.5) = 0.5 + (4/7 - 5/10) = 0.5 + (40/70 - 35/70) = 0.5 + (5/7)/10
    5/7 = 0.7 + (5/7 - 0.7) = 0.7 + (5/7 - 7/10) = 0.7 + (50/70 - 49/70) = 0.7 + (1/7)/10
    '''
    encountered_numers = [1]
    decimal_cycle = list()
    is_cycle = False    
    
    cur_numer, cur_dec = get_next_numer_and_decimal(1, n) 
    if not cur_numer == 0:
        
        while not is_cycle:
        
            if cur_numer in encountered_numers:
                decimal_cycle.append(cur_dec)
                is_cycle = True
            else:
                encountered_numers.append(cur_numer)
                decimal_cycle.append(cur_dec)
                cur_numer, cur_dec = get_next_numer_and_decimal(cur_numer, n) 

            
    return encountered_numers, decimal_cycle

def recip_cycle(n): 
    #e.g. cycle length of 3 is 1 since 1/3 = .(3)
    # cycle length = 7 is 6 since 1/7 = 0.(142857) 
    '''
    how do I know 3 is repeating? 
    1/3 = 0.3 + (1/3 - 0.3) = 0.3 + (1/3 - 3/10) = 0.3 + (10/30 - 9/30) = 0.3 + (1/3)/10. 
    
    What about 1/7 = 0.(142857) 
    1/7 = 0.1 + (1/7 - 0.1) = 0.1 + (1/7 - 1/10) = 0.1 + (10/70 - 7/70) = 0.1 + (3/7)/10
    3/7 = 0.4 + (3/7 - 0.4) = 0.4 + (3/7 - 4/10) = 0.4 + (30/70 - 28/70) = 0.4 + (2/7)/10
    2/7 = 0.2 + (2/7 - 0.2) = 0.2 + (2/7 - 2/10) = 0.2 + (20/70 - 14/70) = 0.2 + (6/7)/10
    6/7 = 0.8 + (6/7 - 0.8) = 0.8 + (6/7 - 8/10) = 0.8 + (60/70 - 56/70) = 0.8 + (4/7)/10
    4/7 = 0.5 + (4/7 - 0.5) = 0.5 + (4/7 - 5/10) = 0.5 + (40/70 - 35/70) = 0.5 + (5/7)/10
    5/7 = 0.7 + (5/7 - 0.7) = 0.7 + (5/7 - 7/10) = 0.7 + (50/70 - 49/70) = 0.7 + (1/7)/10
    '''
    encountered_numers = [1]
    decimal_cycle = list()
    is_cycle = False    
    
    cur_numer, cur_dec = get_next_numer_and_decimal(1, n) 
    while not is_cycle and not cur_numer == 0:
    
        if cur_numer in encountered_numers:
            decimal_cycle.append(cur_dec)
            is_cycle = True
        else:
            encountered_numers.append(cur_numer)
            decimal_cycle.append(cur_dec)
            cur_numer, cur_dec = get_next_numer_and_decimal(cur_numer, n) 
    
        if cur_numer == 0:
            decimal_cycle = list() 
            
    return encountered_numers, decimal_cycle
    

def longest_cycle(max_n):
    candidates = {i for i in range(1,max_n + 1)}
    max_len = 0
    max_loc = 0
    max_numer_cycle = None
    max_dec_cycle = None
    
    for i in candidates:
        cur_numer_cycle, cur_dec_cycle = recip_cycle(i)
        cur_len = len(cur_numer_cycle)
        if cur_len > max_len:
            max_len = cur_len
            max_loc = i
            max_numer_cycle = cur_numer_cycle
            max_dec_cycle = cur_dec_cycle
            
    return max_loc, max_len, max_numer_cycle, max_dec_cycle
    
#f = get_factorization(1000)
#a = get_divisors(f)
#print(a)

#a = longest_cycle(1000)
#print(len(a))

#a,b = get_next_numer_and_decimal(1,5)
#print(a,b)

'''
number = 4
a,b = recip_cycle(number)

print(number)
print(a)
print(b)
#'''


#'''
number = 1000
start = time.time()
max_location, max_length, max_num_cycle, max_decim_cycle = longest_cycle(number)
end = time.time()
print("The maximum lenth numerator cycle is: {}\n\n"
      "The associated decimal cycle is: {}\n\n"
      "Thus the maximum cycle length is {}.\n"
      "and it occurs for the number {}.\n\n"
      "\nTook {} seconds.\n".format(max_num_cycle, max_decim_cycle, max_length, max_location, end-start))

#'''