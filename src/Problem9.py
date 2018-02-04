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

Set c = 1000 - (a+b).
Then a^2 + b^2 = c^2 reduces to (a-1000) * (b-1000) = 5 * 10^5 = 5^6 * 2^5
"""

total_5_power = 6
total_2_power = 5

triplet_found = False

'''
for i in range(total_2_power + 1):
    for j in range(total_5_power + 1):
        print("found triplet = ", triplet_found)
        print()
        print("\nAt i =", i, " j = ", j, ":")
        a_ = -pow(2,i) * pow(5,j)
        b_ = -pow(2,total_2_power - i) * pow(5, total_5_power-j)
        print("a_ = ", a_, "\nb_ = ", b_)
        if -1000 < a_ and a_ < b_: #continue if these hold, else move on
            a = 1000 + a_
            b = 1000 + b_
            c = 1000 - (a + b)
            print(a,b,c)
            if c > b: #QED, else move on
                triplet_found = True
                triplet = [a, b, c]
                print(triplet)
'''
              
#a' = - 2^i * 5^j
#b' = - 2^(5-i) * 5^(6-j)

# check all possible 2-factorizations a' * b' = 5^6 * 2^5
    # ensure -1000 < a' < b' < 0 (note in my algorithm b' < 0 forced by - signs)
    # check if c = 1000 - (a+b) > b
    # if so, QED
    
#'''

for i in range(total_2_power + 1):
    in_range_j_set = {}
    if i == 0 or i == total_2_power:
        in_range_j_set = {2,3,4}
    else:
        in_range_j_set = {3}
    for j in in_range_j_set:
        if pow(25, 3-j) < pow(4, i-2): #continue, else wont have a_ < b_
            print("\nAt i =", i, " j = ", j, ":")
            a_ = -pow(2,i) * pow(5,j)
            b_ = -pow(2,total_2_power - i) * pow(5, total_5_power-j)
            print("a_ = ", a_, "\nb_ = ", b_)
            if -1000 < a_ and a_ < b_: #continue if these hold, else move on
                a = 1000 + a_
                b = 1000 + b_
                c = 1000 - (a + b)
                print(a,b,c)
                if c > b: #QED, else move on
                    triplet_found = True
                    triplet = [a, b, c]
                    print(triplet)
                    print("The product is:", a*b*c)
            print("found triplet = ", triplet_found)
#'''
