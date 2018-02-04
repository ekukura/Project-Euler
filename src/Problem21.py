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
    if num % divisor == 0:
        cur_exp = 1
        num = int( num / divisor )
        while num % divisor == 0:
            cur_exp += 1
            num = int (num / divisor)
        
        return cur_exp
    
    else:
        return 0
    
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
            order = get_divisor_exponent(remaining_num, next_factor)
            my_factors[next_factor] = order
            remaining_num = int(remaining_num / math.pow(next_factor,order))
        
    return my_factors

### the below is incorrect
'''
def get_prime_factors(n):
    
    prime_factors = dict()
    max_possible_prime_factor = int(math.floor(math.sqrt(n)))
    print(max_possible_prime_factor)
    cur_factor = 2;
    cur_num = n
    
    while cur_factor <= max_possible_prime_factor and cur_num > 1:
        print("cur_num is:", cur_num)
        exp = get_divisor_exponent(cur_num, cur_factor)
        print("The exponent for {} is {}".format(cur_factor, exp))
        if exp > 0:
            prime_factors[cur_factor] = exp
            cur_num = int( cur_num / math.pow(cur_factor, exp) )
        if cur_factor == 2:
            cur_factor += 1
        else:
            cur_factor += 2
        
        
    return prime_factors
'''    

def get_all_divisors(factor_dict):
    cur_factor, cur_exponent = factor_dict.popitem()
    
    if len(factor_dict) == 0:
        divisor_set = {int(math.pow(cur_factor, power)) for power in range(cur_exponent + 1)}
            
    else:
    
        remaining_divisors = get_all_divisors(factor_dict)
        
        divisor_set = set(remaining_divisors)
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

 
#note if (a,b) amicable pair, than (a,c) and (c,b) NOT amicable for any c
def amicable_numbers(L):
    #for a=1:L
    #find d(a) = n and try d(n). If n hasn't already been eliminated from eligible amicable numbers,
    #compute d(n) and if d(n) = a, add a and n to amicable pairs; remove
    #n from set to try; increment a
    candidates = {i for i in range(2,L+1)}
    amicable_numbers = set()
    
    while len(candidates) > 0:
        cur_candidate = candidates.pop()
        cur_eligible_mate = d(cur_candidate)
        if cur_eligible_mate in candidates and cur_candidate == d(cur_eligible_mate):
            amicable_numbers = set.union(amicable_numbers, {cur_candidate, cur_eligible_mate})
            candidates.remove(cur_eligible_mate)
            

    return amicable_numbers

num = 10000

start = time.time()
am_nums = amicable_numbers(num)
res = sum(am_nums)
end = time.time()

print("The amicable numbers under {} are \n{}.\nTheir sum is {}\n".format(num, am_nums, res))
print("Took {} seconds".format(end-start))

#print(d(220))
#print(d(284))


'''
For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
'''

#'''
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




'''
l = {3:5, 4:2}
k1, v1 = l.popitem()
print(l)
k2, v2 = l.popitem()
print(l)
print(len(l))
#'''



'''
print(math.pow(2,3)*math.pow(3,2)*5*math.pow(7,4))
res = get_prime_factors(864360)
print(res)
k,v = res.popitem()
#a = res.pop(2)
print(res)
print(k,v)
new_dict = dict(res)
print(new_dict)
#'''



'''
my_set = {1,3,7}
a = my_set.pop()
print(a)
print(my_set)
my_set.remove(7)
print(my_set)
my_set.add(6)
print(my_set)
my_set = set.union({8,17}, my_set)
print(my_set)
print(17 in my_set)
new_set = set(my_set)
print("new set is:\n", new_set)
factor_set = {3*el for el in new_set}
print(factor_set)

#'''

