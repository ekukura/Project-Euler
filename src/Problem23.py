#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:11:33 2017

@author: emilykukura

A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
 it can be shown that all integers greater than 28123 can be written as the sum of two 
 abundant numbers. However, this upper limit cannot be reduced any further by analysis 
 even though it is known that the greatest number that cannot be expressed as the sum 
 of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two 
abundant numbers.

"""
import math, time

LIMIT = 28123
# call numbers which can be written as sum of two abundant #'s  abundant sums
# and those that cannot be as non-abundant sums
# since largest possible non-abundant sum is 28123, only care about abundant #'s 
# <= 28122

#print(get_all_abundants(28122))
#print(isAbundant(2))



#returns all non-abundant sums <= limit
def get_non_abundant_sums(limit):
    non_abundant_sums = {1}
    abundant_sums = get_all_abundants(limit - 1)
    print(abundant_sums)
    for i in range(2,limit + 1):
        is_two_summable = set_two_summable(i , abundant_sums)
        if not is_two_summable:
            non_abundant_sums = set.union(non_abundant_sums, {i})
    
    return non_abundant_sums

#returns True if target_sum can be as sum of two numbers from
#component_set, and false otherwise
def set_two_summable(target_sum, component_set):
    remaining_set = set(component_set)
    sum_found = False
    while len(remaining_set) > 0 and not sum_found:
        cand = remaining_set.pop()
        cand_partner = target_sum - cand
        if cand_partner == cand or cand_partner in remaining_set:
            #print("cand = {}, cand_partner = {}".format(cand, cand_partner))
            sum_found = True
            
            
    return sum_found

#return all abundant numbers < limit
def get_all_abundants(limit):
    abundants = set()
    for i in range(2,limit+1):
        #print("\ni = {}:".format(i))
        if isAbundant(i):
            #print("{} is abundant\n".format(i))
            abundants = set.union(abundants, {i})
    return abundants

num = LIMIT
#sums = get_all_abundants(num - 1)
#print(sums)

'''
print(sums)
print(num)
print(isAbundant(1976))
print(d(1976))
print(isAbundant(26145))
print(d(26145))
print(set_two_summable(28121, sums))
#'''

#'''
start = time.time()
non_abundant_sums = sorted(get_non_abundant_sums(num))
#print("\nThe non-abundant sums are:\n")
#print(non_abundant_sums)
#print("\nThere are {} non-abundant sums".format(len(non_abundant_sums)))
res = sum(non_abundant_sums)
end = time.time()
print("\nResult is: {}\nTook {} seconds.".format(res, end-start))
#'''

def isAbundant(candidate):
    if d(candidate) > candidate:
        return True
    else:
        return False


#returns sum of proper divisors of num, num should be >= 2
def d(num):
    prime_factorization = get_factorization(num)
    #print(prime_factorization)
    divisor_set = get_divisors(prime_factorization)
    divisor_set.remove(num)
    res = sum(divisor_set)
    #print("d({}) = {}\n".format(num,res))
    return res


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




'''
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

num = 284
#num = 2*2*2*3*5*5
print(num)
fac = get_factorization(num)
print(fac)
div = get_divisors(fac)
print(div)
print(d(220))
     
#print(isAbundant(10))
'''





