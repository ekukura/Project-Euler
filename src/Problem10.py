#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:18:26 2017

@author: emilykukura

Find the sum of the primes smaller than 2 million.

"""


import math, time

    
def isPrime1(x):
    foundComposite = False
    if x == 2:
        return True
    else:   
        max_divisor = math.floor(math.sqrt(x))
        
        pdl = [j for j in range(2, max_divisor+1)]
        i = pdl[0]

        while i <= max_divisor and not foundComposite:


            #testing all possible lower divisors
            if x % i == 0:
                foundComposite = True
            else:
                max_k = math.floor(max_divisor / i)
                for k in range(1, max_k + 1):
                    try:
                        pdl.remove(k*i)
                    except:
                        pass
                
                if len(pdl) > 0:
                    i = pdl[0]
                else:
                    i = max_divisor + 1
                
                
        return not foundComposite
    

def isPrime(x):
    foundComposite = False
    if x == 2:
        return True
    elif  x % 2 == 0:
        return False
    else:   
        i = 3
        while i <= math.floor(math.sqrt(x)) and not foundComposite:
            #testing all possible lower divisors
            if x % i == 0:
                foundComposite = True
            i += 1
        return not foundComposite

def determine_primes2(max_x):
    
    if max_x < 2:
        return "no primes"
    elif max_x == 2:
        return [2]
    
    max_divisor = math.floor(math.sqrt(max_x))
    
    #pps = [j for j in range(2, max_x+1)]
    pps = [2]
    pps.extend([2*j+1 for j in range(1, math.floor((max_x+1)/2))])
    prime_index = 1
    cur_prime = pps[prime_index]


    while cur_prime <= max_divisor:
        print(cur_prime)
        #print(cur_prime)
        #remove all possible multiples       
        max_k = math.floor(max_x / cur_prime)

        for k in range(2, max_k + 1):
            try:
                pps.remove(k*cur_prime)
            except:
                pass
        
        #print(pps)
        prime_index += 1
        cur_prime = pps[prime_index]
       
    return pps
    

def determine_primes(max_x):
    
    if max_x < 2:
        return "no primes"
    elif max_x == 2:
        return [2]
    
    max_divisor = math.floor(math.sqrt(max_x))
    
    #pps = [j for j in range(2, max_x+1)]
    pps = {2}
    pps = set.union(pps, {2*j+1 for j in range(1, math.floor((max_x+1)/2))})
    
    found_primes = set()
    cur_prime = min(pps)  

    while cur_prime <= max_divisor:
        
        found_primes = set.union(found_primes, {cur_prime})

        #remove all possible multiples       
        max_k = math.floor(max_x / cur_prime)
        multiples = {k*cur_prime for k in range(cur_prime, max_k+1)}
        pps = pps - multiples
      
        cur_prime = min(pps - found_primes)
       
    return pps
    
    
def sum_primes(max_x):
    p_sum = 0
    for i in range(2, max_x):
        if isPrime(i):
            p_sum += i
            
    return p_sum

if __name__ == '__main__':
    start = time.time() 
    max_num = 2000000
    
    primes = determine_primes(max_num)
    #print(primes)
    res = sum(primes)
    print("sum is:", res)
    print("Took:", round(time.time() - start, 6), "seconds")
    #sum is: 142913828922
    #Took: 9.498652 seconds





#testing
'''
#max_num = 10
#max_num = 400000
max_num = 2000000
res = sum_primes(max_num)
print(res)
print("Took:", round(time.time() - start, 6), "seconds")
#took 76.99175 seconds
'''



""" time test
num = 179426549

start = time.time()
print(isPrime(num))
end = time.time()
time1 = end - start
print(time1)

print()

start2 = time.time()
print(isPrime2(num))
end2 = time.time()
time2 = end2 - start2
print(time2)
"""