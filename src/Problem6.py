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
start = time.time()

########################
# Method 1: Brute Force
########################
n = 600

"""
def sum_of_squares(max_int):
    curSum = 0
    for i in range(max_int):
        curSum += pow((i+1),2)
    return curSum

def squared_sum(max_int):
    curSum = 0
    for i in range(max_int):
        curSum += i+1
    return pow(curSum, 2)

end = time.time()
print(squared_sum(n)-sum_of_squares(n))
#"""

########################
# Method 2: Using Math 
########################
#e.g. sum(i^2, i=1..n) - (sum(i, i=1..n)^2) = 2*sum(i*j, i<j<=n)

"""
curSum = 0
for j in range(2,n+1):
    for i in range(1,j):
        #e.g. when j = 5, want i from 1 to 4
        curSum += i*j
 
end = time.time()       
print(2*curSum)
#"""


############################
# Method 3: Using Recursion 
############################

#"""
def f(max_val):
    if max_val == 1:
        return 0
    else:
        return f(max_val-1) + pow(max_val, 2)*(max_val-1)
 
end = time.time()  
print(f(n))
#"""
        

############################
# Method 3: Identities
############################

"""
squared_sum = pow(n*(n+1)/2,2)
sum_of_squares = n*(n+1)*(2*n+1)/6

end = time.time()  
print(int(squared_sum - sum_of_squares))
#"""

print("time:", end-start)  