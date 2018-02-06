#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:06:07 2017

@author: emilykukura
"""

'''
Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.

e.g. for n = 10: 
sum(i^2, i=1..10) = 385
sum(i, i=1..10)^2 = 55^2 = 3025
So diff = 3025-385 = 2640
'''

import time

def solution_1(n):
########################
# Method 1: Brute Force
########################

    def sum_of_squares(max_int):
        curSum = 0
        for i in range(max_int):
            curSum += pow((i+1),2)
        return curSum
    
    def squared_sum(max_int):
        curSum = 0
        for i in range(1,max_int+1):
            curSum += i
        return pow(curSum, 2)
    
    return squared_sum(n)-sum_of_squares(n)



def solution_2(n):
############################
# Method 2: Using Recursion 
############################

#note diff(n) = (1+2+...+ (n-1) + n)^2 - (1^2+2^2+...+(n-1)^2+n^2) 
# = (1+2+...+(n-1))^2 + n^2 + 2*(1+2+...+(n-1))*n - (1^2+...+(n-1)^2) - n^2
# = (1+2+...+(n-1))^2 - (1^2+...+(n-1)^2) + 2*(1+2+...+(n-1))*n
# = diff(n-1) + 2*(n*(n-1))/2 * n = diff(n-1) + n^2*(n-1)
# (Last line using ID sum(1...m) = m*(m+1)/2

    def diff(max_val):
        if max_val == 1:
            return 0
        else:
            return diff(max_val-1) + pow(max_val, 2)*(max_val-1)
     
    return diff(n)


def solution_3(n):
############################
# Method 3: Identities
############################

    squared_sum = pow(n*(n+1)/2,2)
    sum_of_squares = n*(n+1)*(2*n+1)/6
    
    return squared_sum - sum_of_squares
    
      
if __name__ == '__main__':
    
    start = time.time()
    res_1 = solution_1(100)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start)) 
    
    start = time.time()
    res_2 = solution_2(100)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))   
    
    start = time.time()
    res_3 = solution_3(100)
    end = time.time()
    print("res_3 = {}\nTook {} seconds".format(res_3, end-start)) 
    
    #Answer: 25164150
    
