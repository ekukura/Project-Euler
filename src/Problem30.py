#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:53:59 2017

@author: emilykukura

Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

(I will call these n-summable numbers)

"""

import time, itertools

#returns a maximum on the digit-length of n-summable numbers
#note that if 9^n < (10^(k-1))/k, then for a k-digit number 
#a_k = (d1,d2,...,dk), where di is the i-th digit, we have that
#k <= sum((di)^n, i=1..k)  <= sum(9^n, i=1..k) = k*9^n < 10^(k-1) < a_k
#so that a_k is NOT n-summable. Thus k-1 for the largest such k gives an upper
#bound on the digit-length of n-summable numbers
def get_max(n):
    found_max = False
    k = 2
    while not found_max:
        if pow(9,n) < pow(10, k-1)/k:
            found_max = True
            the_max = k-1
        else:
            k += 1
    return the_max


#returns list - representation of a number, e.g. get_num_list(123) = [3,2,1]
def get_num_list(num):
    num_list = []
    length = len(str(num))
    cur_num = num
    #pick off numbers one at a time.
    for i in range(length):
        cur_digit = cur_num % 10 #e.g. for 123 returns 3
        num_list.append(cur_digit)
        cur_num = int((cur_num - cur_digit) / 10)
        
    return num_list

#returns the n-power-sum of a numbers digits
#e.g. given a_k = (d1,d2,...,dk), returns sum((di)^n, i=1..k)
def get_n_sum_digits(num, n):
    num_list = get_num_list(num)
    #print("The number list is\n", num_list, "\n")
    n_power_list = [pow(num_list[i], n) for i in range(len(num_list))]
    #print("The n-power list is\n", n_power_list, "\n")
    return int(sum(n_power_list))

#returns the set of numbers that can be written as the sum of n-th power of 
#their digits
def get_numbers_brute(n):
    nums = []
    #if n == 4:
    #    nums = [1634, 8208, 9474];
    m = get_max(n) #now only need to look at k-digit numbers for k between 2 and m
    min_num = 10
    max_num = int(pow(10, m)) - 1
    for num in range(min_num, max_num + 1):
        if num % 200000 == 0:
            print("on num = {}\n".format(num))
        if num == get_n_sum_digits(num, n):
            nums.append(num)
            print("number {} has n-power-sum {}\n".format(num, num))

    return nums

#return l-1 for smallest l s.t. l^n > 10^k
#assumed k,n >= 1
def get_max_val(k,n):
    l = 1
    max_found = False
    smallest_large = pow(10,k) #first number that is > k-digits long
    while not max_found:
        if pow(l,n) > smallest_large:
            max_found = True
        else:
            l += 1
    return l-1

def get_num_from_tuple(num_tuple):
    length = len(num_tuple)
    num = 0
    for j in range(length):
        num += num_tuple[length-1 - j]*pow(10, j) #starting from last digit (ones) and going backwards
    
    return num

#returns the sum of numbers that can be written as the sum of n-th power of 
#their digits
def get_sum_brute(n):
    nums = get_numbers_brute(n)
    print("the {}-power-summable numbers are:\n{}\n".format(n,nums))
    res = sum(nums)
    return res


def get_numbers_clever(n): #also, can additionally ignore symmetry
    nums = []
    #if n == 4:
    #    nums = [1634, 8208, 9474];
    m = get_max(n) #now only need to look at k-digit numbers for k between 2 and m
    for k in range(2, m+1):
        max_val = min(get_max_val(k,n), 9)
        num_set = {el for el in itertools.product(range(max_val+1), repeat = k)}

        for el in num_set: 
            if el[0] > 0: #if el starts with 0, ignore (since corr. to < k digit number)
                if k > n and el[0] >= k:
                    pass
                else:
                    num = get_num_from_tuple(el)
                    if num == get_n_sum_digits(num, n):
                        nums.append(num)
                        print("el = {}\n".format(el))
                        print("number {} has n-power-sum {}\n".format(num, num))

    return nums

#returns the sum of numbers that can be written as the sum of n-th power of 
#their digits
def get_sum_clever(n):
    nums = get_numbers_clever(n)
    print("the {}-power-summable numbers are:\n{}\n".format(n,nums))
    res = sum(nums)
    return res


n = 5
#'''
start = time.time()
res = get_sum_brute(n)
end = time.time()
print("The result is {}.\nTook {} seconds".format(res, end-start))
#'''

#'''
start = time.time()
res = get_sum_clever(n)
end = time.time()
print("The result is {}.\nTook {} seconds".format(res, end-start))

#'''


'''
a = get_max_val(2,4)
b = get_max_val(3,4)
print(a,b)
#'''


'''
s = {el for el in itertools.product(range(3), repeat = 3)}
print(s)
#a = list(s.pop())
a = s.pop()
print(a)
#print(len(a))
#print(a[0], a[1], a[2])
print(get_num_from_tuple(a))
a = s.pop()
print(a, get_num_from_tuple(a))
a = s.pop()
print(a, get_num_from_tuple(a))
#'''

#print(get_n_sum_digits(1634, 4))
#print(len(str(123)))

'''
#print(pow(10/9, 34))
for i in range(2,40):
    print(i, get_max(i))
'''




