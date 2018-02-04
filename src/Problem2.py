#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:26:26 2017

@author: emilykukura
"""
#sum of even valued terms <= 4 million in fibonnaci sequence
#f(n) = f(n-1) + f(n-2) 
#Initial Conditions: f(1) = 1, f(2) = 2

import time
'''
note that since odd + even = odd and odd + odd = even,
terms go by pattern o e o o e o o e ... etc.
so that even terms area exactly f(3n+2)'s

From this can derive recurrence:
f(3n+2) = 4*f(3(n-1)+2) + f(3(n-2)+2)
'''

########################
#Solution 1
# uses roots of gf
########################
import math

def f(n):
    alpha = (1 + math.sqrt(5))/2
    beta = (1 - math.sqrt(5))/2
    return round((alpha**(n+1)-beta**(n+1))/math.sqrt(5))

start = time.time()
i = 2
mySum = 0
curVal = f(2)
done = False
while not done :
    mySum += curVal
    i += 3
    curVal = f(i)
    if (curVal > 1000000):
        done = True

print('The sum computed with',
      'solution 1 is', mySum, 'computed in',
      time.time()-start)
#testing
#f_arr = [f(i) for i in range(10)]
#print(f_arr)

##########################
#Solution 2
# brute force/recursion
# (simplified)
##########################

#'''

def g(n):
    if n == 0:
        return 2
    elif n == 1:
        return 8
    else:
        return 4*g(n-1) + g(n-2)

start = time.time()    
i = 0
mySum = 0
curVal = g(0)
while (curVal <= 1000000):
    mySum += curVal
    i += 1
    curVal = g(i)
#'''   
print('The sum computed with',
      'solution 2 is', mySum, 'computed in', 
      time.time()-start)
    
