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
def solution_1(n,m):
    #n is width, m is height, assume want to go from top left to bottom right
    #need n rights, m downs out of (n+m) total moves
    #so (n+m) choose n (or choose m)
    #recall (a choose b) is a!/(b!(a-b)!)
    res = math.factorial(n+m)/(math.factorial(m)*math.factorial(n))
    return int(res)

######################
# recursive solutions
######################

# If you move 1 step right along the lattice, then to travel remainder need solution_3(n-1,m) 
# Similarly, if you move 1 step down along the lattice, then to travel remainder need solution_3(n,m-1) 
def solution_2(n,m):
    if n == 0 or m == 0:
        return 1
    else:
        return solution_3(n-1,m) + solution_3(n,m-1)
    
#recursive solution from two steps out instead of 1 step out like in solution_3
def solution_3(n,m):
    if n == 0 or m == 0:
        return 1
    elif n == 1:
        return m
    elif m == 1:
        return n
    else:
        return solution_3(n-2,m) + solution_3(n,m-2) + 2*solution_3(n-1, m-1)
    
#the same as solution_3 except keeps track of knowledge its already obtained in dictionary d
def solution_4(n,m,d):
    if n == 0 or m == 0:
        return 1
    elif (n,m) in d:
        return d[(n,m)]
    else:
        d[(n,m)]= solution_4(n-1, m, d) + solution_4(n , m-1, d)
        return d[(n,m)]



if __name__ == '__main__':   
    
    n = 20
    m = n
    
    start = time.time()
    res_1 = solution_1(n,m)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start)) 
    
    ''' takes too long for n = m >= 13 (at n = m = 13, ~4 seconds)
    start = time.time()
    res_2 = solution_2(n,m)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))  
    #'''
    
    ''' takes too long for n = m >= 17 (at n = m = 17, ~4 seconds)
    start = time.time()
    res_3 = solution_3(n,m)
    end = time.time()
    print("res_3 = {}\nTook {} seconds".format(res_3, end-start)) 
    #'''
    
    d = {}
    start = time.time()
    res_4 = solution_4(n,m,d)
    end = time.time()
    print("res_4 = {}\nTook {} seconds".format(res_4, end-start))  
        
    #Answer: 137846528820