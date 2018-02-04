#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:51:33 2017

@author: emilykukura

A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the 
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

#put 54 into 10 classes of 10
#class 5, then 54-class_num*class size remain

import math, time

#res = math.factorial(10)

#returns the n-th lex. perm of the numbers in number_set
def get_lex_perm(number_set, ind):
    #print("\n\nget_lex_perm called with arguments:\nnumber_set = {}\nind =  {}\n".format(number_set, ind))
    num_classes = len(number_set)
    number_list = sorted(number_set)
    total_perms = math.factorial(num_classes)
    class_size = int(total_perms / num_classes)
    ind_class = math.floor(ind / class_size)
    the_class = number_list[ind_class]
    remaining_ind = ind - (class_size * ind_class)
    remaining_nums = set(number_set)
    remaining_nums.remove(the_class)
    
    #print("num_classes = {}\ntotal_perms = {}\nclass_size = {}\n".format(num_classes, total_perms, class_size))
    #print("ind_class = {}\nthe_class = {}\nremaining_ind = {}\n".format(ind_class, the_class, remaining_ind))
    
    res = [the_class]
    #print("len(remaining_nums) = ", len(remaining_nums))
    
    if len(remaining_nums) > 0:
        res.extend(get_lex_perm(remaining_nums, remaining_ind))
    
    #print("\nres when number_set = {} is {}\n".format(number_set, res))
    
    return res

numbers = {i for i in range(10)}
num = 1000000

#numbers = {i for i in range(4)}
#num = 8
#0123, 0132, 0213, 0231, 0312, 0321
#1023, 1032, 1203, 1230, 1302, 1320
#2013, 2031, 2103, 2130, 2301, 2310
#3012, 3021, 3102, 3120, 3201, 3210

start = time.time()
res = get_lex_perm(numbers, num-1)
end = time.time()
print("\nres = {}. Took {} seconds".format(res, end-start))






#a = [1,2]
#a.extend([3,4])
#print(a)