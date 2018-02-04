#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:14:04 2017

@author: emilykukura

How many lattice paths (right/down) from top left to bottom right point
in 20x20 grid

"""
import math, time

#simple solution using combinatorics
def lattice(n,m):
    #n is width, m is height, assume want to go from top left to bottom right
    #need n rights, m downs out of (n+m) total moves
    #so (n+m) choose n (or choose m)
    #recall (a choose b) is a!/(b!(a-b)!)
    res = math.factorial(n+m)/(math.factorial(m)*math.factorial(n))
    return int(res)

#recursive solutions
def lattice2(n,m):
    #print("lattice 2 called with n = ", n, "and m = ", m)
    if n == 0 or m == 0:
        return 1
    else:
        return lattice2(n-1,m) + lattice2(n,m-1)
    
def lattice3(n,m):
    if n == 0 or m == 0:
        return 1
    elif n == 1:
        return m
    elif m == 1:
        return n
    else:
        return lattice2(n-2,m) + lattice2(n,m-2) + 2*lattice(n-1, m-1)
    
def lattice4(n,m,d):
    #print("lattice 2 called with n = ", n, "and m = ", m)
    #print("at beginning of execution, n =", n, "m = ", m, "and d = ", d, "\n")
    if n == 0 or m == 0:
        return 1
    elif (n,m) in d:
        return d[(n,m)]
    else:
        d[(n,m)]= lattice4(n-1, m, d) + lattice4(n , m-1, d)
        return d[(n,m)]

'''
d = {(0,0):1, (0,1):1, (1,0):1}
print(d)
print(d[(0,1)])
'''

n = 40
m = n
start = time.time()
print(lattice(n,m))
print("took", time.time()-start, "seconds")

d = {}
start = time.time()
print(lattice4(n,m,d))
print("took", time.time()-start, "seconds")

'''
start = time.time()
print(lattice3(n,n))
print("took", time.time()-start, "seconds")    
'''

'''
start = time.time()
print(lattice2(n,m))
print("took", time.time()-start, "seconds")
'''



