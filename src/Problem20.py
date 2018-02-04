#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:16:47 2017

@author: emilykukura

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import numpy as np
import math
import time

def rec_factorial(n):
    if n < 1:
        print("factorial(a) for a <= 0 is undefined")
        return None
    if n == 1:
        return 1
    else:
        return n*rec_factorial(n-1)

def array_factorial(n): #return factorial in array form:
    if n < 1:
        print("factorial(a) for a <= 0 is undefined")
        return None
    if n == 1:
        return np.array([1])
    else:
        return array_mult(array_factorial(n-1), n)
        
    

def array_mult_factor_under_10(arr, factor): # e.g. arr = [4,2,6], factor = 3, desired output: [1,2,7,8]
    #print("array_mult called with arguments")
    #print("arr = ", arr)
    #print("factor = ", factor)
    n = len(arr) 
    new_arr = np.array([], dtype = np.int)
    carry = 0
    for pos in range(n-1,-1,-1):            #pos = 2        pos = 1
        cur_el = arr[pos]                   #cur_el = 6     cur_el = 2
        total = factor * cur_el + carry     #total = 18     total = 6+1= 7
        resid = total % 10                  #resid = 8      resid = 7
        carry = int(math.floor(total/10))   #carry = 1      carry = 0
        new_arr = np.insert(new_arr, obj = 0, values = resid)
        #print(new_arr)                      #new_arr = [8]  new_arr = [7,8]
        
        if pos == 0 and carry > 0: #if in last position and carry is not 0, insert carry at front                                    
            new_arr = np.insert(new_arr, obj = 0, values = carry)
            #print(new_arr)
            
    return new_arr

def array_mult(arr, factor): # e.g. arr = [4,2,6], factor = 3, desired output: [1,2,7,8]
    #print("array_mult called with arguments")
    #print("arr = ", arr)
    #print("\nfactor = ", factor)
    n = len(arr) 
    new_arr = np.array([], dtype = np.int)
    carry = 0
    for pos in range(n-1,-1,-1):            #pos = 2        pos = 1
        cur_el = arr[pos]                   #cur_el = 6     cur_el = 2
        total = factor * cur_el + carry     #total = 18     total = 6+1= 7
        resid = total % 10                  #resid = 8      resid = 7
        carry = int(math.floor(total/10))   #carry = 1      carry = 0
        new_arr = np.insert(new_arr, obj = 0, values = resid)
        #print(new_arr)                      #new_arr = [8]  new_arr = [7,8]
        
        if pos == 0 and carry > 0: #if in last position and carry is not 0, insert carry at front                                    
            '''
            #implementation 1
            carry_str = str(carry)
            for j in range(len(carry_str)-1, -1, -1):
                new_arr = np.insert(new_arr, obj = 0, values = int(carry_str[j]))
                #print(new_arr)
            '''    
            #implementation 2
            #num_digits = math.ceil(math.log10(carry))
            while carry > 0:
                #if num_digits > 1:
                    #print("carry = ", carry)
                to_add = carry % 10
                new_arr = np.insert(new_arr, obj = 0, values = to_add)
                #print(new_arr)
                carry = int((carry - to_add)/10)
            #'''
    return new_arr


n = 100
start1 = time.time()
res = array_factorial(n)
end1 = time.time()
print("res = ", sum(res))
print("Took {} seconds".format(end1-start1))

print()


#'''   
start2 = time.time()
res2 = rec_factorial(n)
res2_string = str(res2)
#print(res2_string)

res2_sum = 0
for i in range(len(res2_string)):
    res2_sum += int(res2_string[i])
 
end2 = time.time()
print("\nresult is {}".format(res2_sum))
print("Took {} seconds".format(end2-start2))

#print(res_string[3])
#'''



'''
arr = [4,2,6]
res = array_mult(arr, 3)
print(res)
'''


'''
print(426*3)
a = np.array([], dtype = np.int)
a = np.insert(a, obj = 0, values = 1)
print(a)
a = np.insert(a, obj = 0, values = 3)
print(a)
'''


'''
m = 10
prod = 1
for i in range(m,0,-1):
    print("prod = ", prod)
    print("i = ", i)
    prod *= i
    
print(prod)
'''