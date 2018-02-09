#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:17:15 2017

@author: emilykukura

What is the sum of the digits of the number 2^1000?

"""

import time

# function which takes a list-representation l of a number n
# and return the list representation of 2*n
# note the list l in reverse of natural order, e.g. # 502 represented by [2,0,5]
# so that double_list([2,0,5]) = [4,0,0,1]
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


#method dynamically builds a powers of two dictionary to get result
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
    

#dynamic, but without dictionary, since once use previous power of two don't need to 
#keep it
def get_digits_dyn2(base, power):
#note this only works for base = 2 right now
#note digit list in reverse of natural order, e.g. # 4,096 represented by [6,9,0,4]
    
    if not base == 2:
        return None
    
    #uses dynamic programming
    prev_list = [1]
    for _ in range(1, power + 1):  
        new_list = double_list(prev_list)
        prev_list = new_list     
        
    return new_list
    

#recursive solution; for power > 900 recursion depth exceeded
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

#direct solution -- easy
def sum_digits_given_num(num):
    str_num = str(num)
    str_digits = list(str_num)
    num_digits = len(str_digits)
    digits = [int(str_digits[i]) for i in range(num_digits)]
    digit_sum = sum(digits)
    return digit_sum

display_color = {
    'red':      "\033[1;31m",
    'off':        "\033[0;0m"
}

def solution_1(two_power):
    res = None ; digit_list = None
    max_rec_depth_exceeded = False
    try:
        digit_list = get_digits(2, two_power)
        res = sum(digit_list)
    except RecursionError as e:
        max_rec_depth_exceeded = True
        print("{}{}{}".format(display_color['red'], e.args[0], display_color['off']))  
    
    return res, digit_list, max_rec_depth_exceeded

def solution_2(two_power):
    digit_list = get_digits_dyn(2, two_power)
    res = sum(digit_list)
    return res, digit_list

def solution_3(two_power):
    digit_list = get_digits_dyn2(2, two_power)
    res = sum(digit_list)
    return res, digit_list

def solution_4(two_power):
    res = sum_digits_given_num(pow(2, two_power))
    return res

if __name__ == '__main__':   
    
    #two_power = 500
    two_power = 1000
    
    start = time.time()
    res_1, _ , rec_depth_exceeded = solution_1(two_power)
    end = time.time()
    if rec_depth_exceeded:
        print("{}{}{}".format(display_color['red'], "No result, recursion depth exceeded.", display_color['off']))  
    else:
        print("res_1 = {}\nTook {} seconds".format(res_1, end-start)) 
    
    start = time.time()
    res_2, _ = solution_2(two_power)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))  

    start = time.time()
    res_3, _ = solution_3(two_power)
    end = time.time()
    print("res_3 = {}\nTook {} seconds".format(res_3, end-start)) 
    
    start = time.time()
    res_4 = solution_4(two_power)
    end = time.time()
    print("res_4 = {}\nTook {} seconds".format(res_4, end-start))  
           
    # Answer: 1366

    
    