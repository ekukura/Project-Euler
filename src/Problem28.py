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

def solution_1(odd):
    k = int((odd-1)/2) #this is the number of nested squares, excluding the center 1
    if k == 0:
        total_diagonals_sum = 1
    else:
        NE_sum = sum([pow(2*i+1,2) for i in range(1,k+1)]) #upper right quadrant
        SE_sum = sum([pow(2*i,2) - (2*i-1) for i in range(1,k+1)]) #lower right quadrant
        SW_sum = sum([pow(2*i,2) + 1 for i in range(1,k+1)]) #lower left quadrant
        NW_sum = sum([pow(2*i+1,2) - 2*i for i in range(1,k+1)]) #upper left quadrant
        total_diagonals_sum = NE_sum + SE_sum + SW_sum + NW_sum + 1  #1 takes care of middle element
        
    return total_diagonals_sum

def solution_2(odd):
    k = int((odd-1)/2)
    if k == 0:
        total_diagonals_sum = 1
    else:
        # derivation for formula: 
        # total_diagonals_sum = 2 * sum([pow(2*i+1,2) + pow(2*i,2) - 2*i + 1 for i in range(1,k+1)]) + 1 
        #    = 2 * sum( (4*i^2 + 4*i + 1) + 4*i^2 - 2*i + 1) for i in range(1, k+1) ) + 1
        #    = 2 * sum( (8*i^2) + 2*i + 2 for i in range(1,k+1) ) + 1     
        #    = (16 * sum( (i^2) : i=1:k) + 4 * sum(i: i=1:k) + 4*k + 1)
        #    = 16 * k(k+1)(2k+1)/6 + 4 * k(k+1)/2 + 4*k + 1
        # (last formula uses closed form for sum(i: i=1:k) = k(k+1)/2
        # and sum(i^2: i=1:k) = k(k+1)(2k+1)/6
        total_diagonals_sum = int(k*(k+1)*( (8/3)*(2*k+1) + 2 ) + 4*k + 1)
        
    return total_diagonals_sum

if __name__ == "__main__":

    num = 1001
    
    start = time.time()
    res_1 = solution_1(num)
    end = time.time()
    print("The sum is {}\nTook {} seconds".format(res_1, end-start))
    
    start = time.time()
    res_2 = solution_2(num)
    end = time.time()
    print("The sum is {}\nTook {} seconds".format(res_2, end-start))
    
    #Answer: 669171001
