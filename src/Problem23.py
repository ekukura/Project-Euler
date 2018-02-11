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
import math, time, itertools

#assumed divisor IS divisor of num
def get_divisor_exponent(num, divisor) :
    exp = 0
    cur_num = num
    while int(cur_num % divisor) == 0:
        exp += 1
        cur_num = int(cur_num / divisor)
    
    return exp


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

#return prime factorization in dictionary form
def get_factorization(num):
    factorization = dict()
    cur_num = num
    min_remaining_factor_cand = 2
    while cur_num > 1 and min_remaining_factor_cand <= cur_num:
        
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
#returns sum of proper divisors of num, num should be >= 2

def d(num):
    prime_factorization = get_factorization(num)
    #print(prime_factorization)
    divisor_set = get_divisors(prime_factorization)
    divisor_set.remove(num)
    res = sum(divisor_set)
    #print("d({}) = {}\n".format(num,res))
    return res
  

def isAbundant(candidate):
    if d(candidate) > candidate:
        return True
    else:
        return False


#return all abundant numbers <= limit
def get_all_abundants(limit):
    abundants = set()
    for i in range(12,limit+1): #since 12 is smallest abundant sum
        #print("\ni = {}:".format(i))
        if isAbundant(i):
            #print("{} is abundant\n".format(i))
            abundants = set.union(abundants, {i})
    return abundants


# Improvement on get_all_abundants
# Thoughts for improvement:
# It's true that isAbundant(n) -> isAbundant(k*n) for any integer k>=1
# And we can use this to improve the get_all_abundants function

# Let factors(n) = {f1, f2, ... , f_d(n), f_[d(n)+1]} be the factors of n, 
# in increasing order (so f_[d(n)+1] = n). 

# Assume d(n) > n.
# Then factors((p^a)*n) = union(p^j * {f1, f2, ... , f_d(n), f_[d(n)+1]}) for j = 0..a)
# So since d(m) = sum(factors(m)) - m, we have:
#
# d((p^a)*n) = sum(p^j * sum(factors(n)), j = 0...a) - (p^a)*n
#            = sum(factors(n) * sum(p^j, j = 0...a) - (p^a)*n
#            = (d(n) + n) * sum(p^j, j = 0...a) - (p^a)*n
#            > 2*n*sum(p^j, j = 0...a) - (p^a)*n
#            > 2*p^a*n - (p^a)*n = (p^a)*n
# 
# However, function below is actually SLOWER
def get_all_abundants_2(limit):
    abundants = set()
    candidates = {i for i in range(12, limit+1)}
    i = 1
    while i <= limit and len(candidates) > 0: #since 12 is smallest abundant sum
        #print("\ni = {}:".format(i))
        i = min(candidates)
        candidates.remove(i)
        if isAbundant(i):
            #print("{} is abundant\n".format(i))
            #get all multiples k*i s.t. k*i <= limit, and remove them
            mult_set = {k*i for k in range(1, int(math.floor(limit/i)) + 1)}
            candidates = candidates - mult_set
            abundants = set.union(abundants, mult_set)           
            
    return abundants


#returns True if target_sum can be as sum of two numbers from
#component_set, and False otherwise
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


#returns all non-abundant sums <= limit
def get_non_abundant_sums(limit):
    non_abundant_sums = {1}
    abundants = get_all_abundants(limit)
    #print(abundant_sums)
    for i in range(2,limit+1):
        is_two_summable = set_two_summable(i , abundants)
        if not is_two_summable:
            non_abundant_sums = set.union(non_abundant_sums, {i})
    
    return non_abundant_sums


#returns all non-abundant sums <= limit
def get_non_abundant_sums_2(limit):

    candidates = {i for i in range(limit+1)}
    abundants = get_all_abundants(limit)
    #Get direct sum of abundant_sums with itself
    abundant_two_sums = {a+b for (a,b) in itertools.product(abundants, abundants)}
    #Then take all numbers <= limit which are NOT in this list
    return candidates - abundant_two_sums


def solution_1(num):
    non_abundant_sums = get_non_abundant_sums(num)
    #print("\nThe non-abundant sums are:\n")
    return sum(non_abundant_sums)

def solution_2(num):
    non_abundant_sums = get_non_abundant_sums_2(num)
    #print("\nThe non-abundant sums are:\n")
    return sum(non_abundant_sums)

if __name__ == '__main__':
    
    LIMIT = 28123
    # call numbers which can be written as sum of two abundant #'s  abundant sums
    # and those that cannot be as non-abundant sums.
    # since largest possible non-abundant sum is 28123, only care 
    # about abundant #'s  <= 28122
    

    num = LIMIT - 1
    #print(isAbundant(1976))
    #print(d(1976))
    #print(get_all_abundants(num - 1))
    
    #A = {1,2,3}
    #dir_sum = {a+b for (a,b) in itertools.product(A,A)}
    #print(dir_sum)
        
    start = time.time()
    res_1 = solution_1(num)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))   
    # time ~ 10.95 s
    
    start = time.time()
    res_2 = solution_2(num)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))  
    # time ~ 6.41 s
    
    # Answer: 4179871





