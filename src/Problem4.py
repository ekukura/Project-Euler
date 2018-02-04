#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 01:04:58 2017

@author: emilykukura
"""
import math, time, itertools
from sqlalchemy.sql.expression import false

'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of 
two 3-digit numbers.
'''
#Answer:  906609
 
#returns all palindromes of specified digit length
def get_all_palindromes(digit_length):
    if digit_length == 0: 
        res_set = {}
    if digit_length == 1:
        res_set = {1,2,3,4,5,6,7,8,9}
    else:
        res_set = {10**(digit_length-1)+1}  #initial element
        #takes care of n0000000n for n from 1 to 9
        for n in range(2,10):
            res_set = res_set | {n*pow(10,digit_length-1)+n}
        #still need to take care of n0....0n for all where not all 0s in between
        #e.g. if digit_length = 9 need:
        max_recursion_level = math.floor((digit_length-1)/2)
        for i in range(1, max_recursion_level + 1):
            #e.g. for digit_length = 9
            #i=1 takes care of nm...mn for n from 1 to 9
            #i=2 takes care of n0tskst0n for n,t from 1 to 9, k,s from 0 to 9
                    #palnidromes(dl - 2*2)
            #i=3 takes care of n00sks00n for n,s from 1 to 9, k from 0 to 9  
                    #palnidromes(dl - 2*3)   
            #i=4  takes care of n000k000n for n,k from 1 to 9
                    #palnidromes(dl - 2*4)
            for n in range(1,10):
                inner_set = get_all_palindromes(digit_length-2*i)
                for el in inner_set:
                    #for debugging:
                    #curEl = n*pow(10,digit_length-1)+ el*pow(10,i) + n
                    res_set = res_set | {n*pow(10,digit_length-1)+ el*pow(10,i) + n}              
                    
    return res_set           

def get_all_palindromes2(digit_length):
    if digit_length == 0: 
        res_set = {}
    if digit_length == 1:
        res_set = {1,2,3,4,5,6,7,8,9}
    elif digit_length == 2:
        res_set = {11,22,33,44,55,66,77,88,99}
    elif digit_length == 3:
        res_set = {101}
        for n in range(1,10):
            for j in range(0,10) :
                res_set = res_set | {n*100+j+n}
    else:
        #this takes care of all of form n0...0n
        res_set = {10**(digit_length-1)+1} 
        for m in range(2,10):
            res_set = res_set | {m*pow(10,digit_length-1)+m}
        smaller_set = get_all_palindromes(digit_length-2)
        smaller4_set = get_all_palindromes(digit_length-4)
        for n in range(1,10):
            for el in smaller_set:
                res_set = res_set | {n*pow(10,digit_length-1)+ el*10 + n}
            for el in smaller4_set:
                res_set = res_set | {n*pow(10,digit_length-1)+ el*100 + n}
    return res_set

def solution():   
    #minNum = 100*100 #10000
    #maxNum = 999*999 #998001
    #thus only need to search for the 5 and 6-digit palindromes
    
    #find set of all palandromes
    palindrome5_set = get_all_palindromes(5)
    palindrome6_set = get_all_palindromes(6)    
    palindrome_set = palindrome5_set | palindrome6_set 
    
    prod_set = {i*j for i, j in itertools.product(range(900,1000), range(900,1000))}
    palindrome_and_prod_set = palindrome_set & prod_set

    res = max(palindrome_and_prod_set) 
    print(res, "is a product palindrome")

def solution2():   
    #minNum = 100*100 #10000
    #maxNum = 999*999 #998001
    #thus only need to search for the 5 and 6-digit palindromes
    
    #find set of all palandromes
    palindrome5_set = get_all_palindromes2(5)
    palindrome6_set = get_all_palindromes2(6)    
    palindrome_set = palindrome5_set | palindrome6_set 
    
    prod_set = {i*j for i, j in itertools.product(range(900,1000), range(900,1000))}
    palindrome_and_prod_set = palindrome_set & prod_set

    res = max(palindrome_and_prod_set) 
    print(res, "is a product palindrome")  

if __name__ == '__main__':    
    start = time.time()    
    solution()
    print("This took", time.time()-start, "seconds.")
    
    start = time.time()    
    solution2()
    print("This took", time.time()-start, "seconds.")  
    





                 
     
 
