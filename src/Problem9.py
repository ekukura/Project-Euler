#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:34:06 2017

@author: emilykukura

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time 

'''      
Since a + b + c = 1000, c = 1000 - (a+b).
Then a^2 + b^2 = c^2 reduces to:
 a^2 + b^2 = (1000 - (a+b))^2 
           = 1000^2 - 2*1000*(a+b) + (a+b)^2 
           = 1000^2 - 2*1000*(a+b) + a^2 + b^2 + 2*a*b
    
 So adding 1000^2 - a^2 - b^2 from both sides we have:
 1000^2 = 2*1000^2 - 2*1000*(a+b) + 2*a*b 
        = 2*(ab - 1000(a+b) + 1000^2)   
        = 2*(a-1000)*(b-1000)

So finally we have:

(1)     (a-1000) * (b-1000) = 5 * 10^5 = 5^6 * 2^5
(2)     a < b < c natural numbers s.t. a + b + c = 1000

Thus we want to find natural numbers a < b s.t. (1) holds. Note since a,b,c natural numbers
The condition (2) forces 0 < a < b < 1000

Now, set a' = a - 1000, b' = b - 1000, so that (1) and (2) become:

(1')    a' * b' = 5^6 * 2^5
(2')    -1000 < a' < b' < 0
(3')    c > b

        
        

Now, since a' and b' are negative integers whose product (by 1')
is 5^6 * 2^5 we can write

    (4')    a' = -2^i * 5^j
    (5')    b' = -2^(5-i) * 5^(6-j)
    
    where 0 <= i <= 5 and 0 <= j <= 6

    Further, since abs(a'); abs(b') < 1000 and 5^5 > 1000, 
    j cannot be 0, 1, 5, or 6, so j in {2,3,4}.
    
    Further, if 0 < i < 5 then since 2 * 5^4 > 1000 (4' and 5') forces j = 3
    
    Finally a' < b' forces 2^i * 5^j > 2^(5-i) * 5^(6-j), or equivalently:
    
    (6')    5^(2j-6) > 2^(5-2i). 
    
    Thus we can go through all possible values of i and j, which are:
    
    when i = 0 or i = 5, 2 <= j <= 4
    when 1 <= i <= 4, j = 3
    
    and for each pair check if condition (6') holds. 
    
    If so, then we also check the remainder of condition (2') 
        -- it suffices to check -1000 < a' since (6') ensures a' < b' 
        and (4'), (5') ensure a', b' < 0
        
    Finally, we check (3') and if so then we have found our pythagorean triple.
        
'''
            
def solution_1():

    total_5_power = 6
    total_2_power = 5
        
    triplet_found = False
    triplet = None
    
    for i in range(total_2_power + 1):
        in_range_j_set = {}
        if i == 0 or i == total_2_power:
            in_range_j_set = {2,3,4}
        else:
            in_range_j_set = {3}
        for j in in_range_j_set:
            if pow(5, 2*j - 6) > pow(2, 5 - 2*i):
                print("\nAt i =", i, " j = ", j, ":")
                a_ = -pow(2,i) * pow(5,j)
                b_ = -pow(2,total_2_power - i) * pow(5, total_5_power-j)
                print("a_ = ", a_, "\nb_ = ", b_)
                if -1000 < a_: #continue if these hold, else move on
                    a = 1000 + a_
                    b = 1000 + b_
                    c = 1000 - (a + b)
                    print(a,b,c)
                    if c > b: #QED, else move on
                        triplet_found = True
                        triplet = [a, b, c]
                        print(triplet)
                        print("The product is:", a*b*c)
                print("found triplet = {}\n".format(triplet_found))
                
    return triplet

              
                
if __name__ == '__main__':  

    start = time.time()
    res_1 = solution_1()
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))  
                


