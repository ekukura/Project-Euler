#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:13:04 2017

@author: emilykukura

Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

"""

import time

def sum_diagonals_spiral(odd):
    k = int((odd-1)/2)
    if k == 0:
        total_diagonals_sum = 1
    else:
        NE_sum = sum([pow(2*i+1,2) for i in range(1,k+1)])
        SE_sum = sum([pow(2*i,2) - (2*i-1) for i in range(1,k+1)])
        SW_sum = sum([pow(2*i,2) + 1 for i in range(1,k+1)])
        NW_sum = sum([pow(2*i+1,2) - 2*i for i in range(1,k+1)])
        total_diagonals_sum = NE_sum + SE_sum + SW_sum + NW_sum + 1
        
    return total_diagonals_sum

def sum_opt(odd):
    k = int((odd-1)/2)
    if k == 0:
        total_diagonals_sum = 1
    else:
        #total_diagonals_sum = 2 * sum([pow(2*i+1,2) + pow(2*i,2) - 2*i + 1 for i in range(1,k+1)]) + 1  
        #total_diagonals_sum = 2 * sum([8*pow(i,2) + 2*i + 2 for i in range(1,k+1)]) + 1     
        #total_diagonals_sum = (16 * sum([pow(i,2) for i in range(1,k+1)]) + 
        #                       4 * sum([i for i in range(1, k+1)]) + 4*k + 1)
        total_diagonals_sum = int(k*(k+1)*( (8/3)*(2*k+1) + 2 ) + 4*k + 1)
        # this final formula uses closed form for sum(i: i=1:k) = k(k+1)/2
        # and sum(i^2: i=1:k) = k(k+1)(2k+1)/6
        
    return total_diagonals_sum
        
num = 1001
start = time.time()
res = sum_diagonals_spiral(num)
end = time.time()
print("The sum is {}\nTook {} seconds".format(res, end-start))
start = time.time()
res2 = sum_opt(num)
end = time.time()
print("The sum is {}\nTook {} seconds".format(res2, end-start))

