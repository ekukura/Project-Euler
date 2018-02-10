#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:16:47 2017

@author: emilykukura

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import numpy as np
import math
import time

def rec_factorial(n):
    if n < 0:
        print("factorial(n) for n < 0 is undefined")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n*rec_factorial(n-1)
    
#multiplies integer represented in array arr by the multiple factor
# e.g. arr = [4,2,6], factor = 3, desired output: [1,2,7,8]
def array_mult(arr, factor):
    n = len(arr) 
    new_arr = np.array([], dtype = np.int)
    carry = 0                               #for case arr = [4,2,6]; factor = 3, we have:
    for pos in range(n-1,-1,-1):            #pos = 2        pos = 1            pos = 0
        cur_el = arr[pos]                   #cur_el = 6     cur_el = 2        cur_el = 4
        total = factor * cur_el + carry     #total = 18     total = 6+1= 7    total = 12 + 0 = 12
        resid = total % 10                  #resid = 8      resid = 7         resid = 2
        carry = int(math.floor(total/10))   #carry = 1      carry = 0         carry = 1
        new_arr = np.insert(new_arr, obj = 0, values = resid) #inserts resid at index 0
        #print(new_arr)                      #new_arr = [8]  new_arr = [7,8]  new_arr = [2,7,8]
        
        if pos == 0 and carry > 0: #if in last position and carry is not 0, insert carry at front                                    
            while carry > 0:
                to_add = carry % 10
                new_arr = np.insert(new_arr, obj = 0, values = to_add)
                #print(new_arr)
                carry = int((carry - to_add)/10)
    return new_arr

def array_factorial(n): #return factorial in array form:
    if n < 1:
        print("factorial(a) for a <= 0 is undefined")
        return None
    if n == 1:
        return np.array([1])
    else:
        return array_mult(array_factorial(n-1), n)
        

def dyn_factorial(n):
    if n < 0:
        print("factorial(n) for n < 0 is undefined")
        res = None
    elif n == 0:
        res = 1
    else:
        cur_index = 2
        res = 1
        while cur_index <= n:
            res *= cur_index
            cur_index += 1
        
    return res
    
def solution_1(n):
    return sum(array_factorial(n))

def solution_2(n):
    res = rec_factorial(n)
    res_string = str(res)
    
    res_sum = 0
    for i in range(len(res_string)):
        res_sum += int(res_string[i])
        
    return res_sum

def solution_3(n):
    res = dyn_factorial(n)
    res_string = str(res)
    
    res_sum = 0
    for i in range(len(res_string)):
        res_sum += int(res_string[i])
        
    return res_sum

if __name__ == '__main__':
    n = 100
    
    start1 = time.time()
    res = solution_1(n)
    end1 = time.time()
    print("res = ", res)
    print("Took {} seconds".format(end1-start1))
    
    start = time.time()
    res2 = solution_2(n)
    end = time.time()
    print("\nres = {}".format(res2))
    print("Took {} seconds".format(end-start))
    
    start = time.time()
    res3 = solution_3(n)
    end = time.time()
    print("\nres = {}".format(res3))
    print("Took {} seconds".format(end-start))

    # Answer: 648

