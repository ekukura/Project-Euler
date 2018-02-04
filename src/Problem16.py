#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:17:15 2017

@author: emilykukura

What is the sum of the digits of the number 2^1000?

"""

import time

MAX_RECURSION_DEPTH = 900

def get_digits_dyn(base, power):
#note this only works for base = 2 right now
#note digit list in reverse of natural order, e.g. # 4,096 represented by [6,9,0,4]
    
    if not base == 2:
        return None
    
    #uses dynamic programming
    d = {0:[1]} #dictionary with lists
    for i in range(1, power + 1):  
        new_list = double_list(d[i-1])
        d[i] = new_list     
        
    return d[power]
    

def get_digits_dyn2(base, power):
#note this only works for base = 2 right now
#note digit list in reverse of natural order, e.g. # 4,096 represented by [6,9,0,4]
    
    if not base == 2:
        return None
    
    #uses dynamic programming
    #d = {0:[1]} #dictionary with lists
    prev_list = [1]
    for i in range(1, power + 1):  
        new_list = double_list(prev_list)
        prev_list = new_list     
        
    return new_list
    

def get_digits(base, power):
    #note digit list in reverse of natural order, e.g. # 4,096 represented by [6,9,0,4]
    
    if power < 0:
        digit_list = None
    elif power == 0:
        digit_list = [1]
    else:
        prev_digit_list = get_digits(base, power-1)
        #num_prev_digits = len(prev_digit_list)
        #print('\n', "power - 1 = ", power - 1, '\n', prev_digit_list, '\n', num_prev_digits)
           
        digit_list = double_list(prev_digit_list)
    
    return digit_list 


def double_list(l):
    
    double_list = list()
    carry_val = 0
    
    length = len(l)
    for i in range(length):
        if i == 0:
            carry_val = 0
                
        cur_val = l[i]
        new_val = 2*cur_val + carry_val
        #print("cur_val = ", cur_val, "new_val = ", new_val)
        
        if new_val < 10:    
            carry_val = 0
            append_val = new_val
        else:
            carry_val = 1
            append_val = new_val % 10
        
        #print("carry_val = ", carry_val, "append_val = ", append_val)
        double_list.append(append_val)
            
        if i == length-1 and carry_val == 1:
            double_list.append(1)
           
        digit_list = double_list    
        
    return digit_list


def sum_digits_given_num(num):
    str_num = str(num)
    str_digits = list(str_num)
    num_digits = len(str_digits)
    digits = [int(str_digits[i]) for i in range(num_digits)]
    digit_sum = sum(digits)
    return digit_sum


'''
l = [6,5,2]
result = double_list(l)
print(result)
'''




#'''
#two_power = 5000
two_power = 1000

'''
start = time.time()
digit_list = get_digits(2, two_power)
end = time.time()

print("result is:", sum(digit_list))
print("took", end-start, "seconds")
'''

start = time.time()
digit_list = get_digits_dyn(2, two_power)
end = time.time()

print("result is:", sum(digit_list))
print("took", end-start, "seconds")

start = time.time()
digit_list = get_digits_dyn2(2, two_power)
end = time.time()

print("result is:", sum(digit_list))
print("took", end-start, "seconds")

start = time.time()
res = sum_digits_given_num(pow(2, two_power))
end = time.time()
print("result is:", res)
print("took", end-start, "seconds")
#'''

####################################

#a = [pow(2,i) for i in range(15)]
#a_strs = [str(a[i]) for i in range(15)]

#s = '412'
#s2 = list(s)
#print(sum_digits_given_num(412))

#for i in range(16):
#    print("i = ", i, "num = ", pow(2,i), "sum = ", sum_digits_given_num(pow(2,i)))

#print(sum_digits_given_num(pow(2,1000)))
#print(pow(2,1000))



'''
l = [4, 0, 9, 6]
l2 = [6,9,0,4]
double_list = list()
carry_val = 0

length = len(l2)

for i in range(length):
    if i == 0:
        carry_val = 0
            
    cur_val = l2[i]
    new_val = 2*cur_val + carry_val
    print("cur_val = ", cur_val, "new_val = ", new_val)
    
    if new_val < 10:    
        carry_val = 0
        append_val = new_val
    else:
        carry_val = 1
        append_val = new_val % 10
    
    print("carry_val = ", carry_val, "append_val = ", append_val)
    double_list.append(append_val)
        
    if i == length-1 and carry_val == 1:
        double_list.append(1)
    
print(double_list)        
'''

    
    