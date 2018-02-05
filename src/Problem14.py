#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:48:39 2017

@author: emilykukura

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
"""

import time

def collatz(n): #one step of collatz sequence
    if n == 1:
        return n
    elif n % 2 == 0:
        return int(n/2)
    else:
        return 3 * n + 1
     
def collatz_seq(n):
    seq = [n]
    cur_num = n
    while not cur_num == 1:
        cur_num = collatz(cur_num)           
        seq.append(cur_num)
        
    return seq

def build_collatz(max_n):
    c = [[], [1]]    
    d = {1:1} #dictionary containing first occurences, e.g. d[i] is the index of the collatz seq i first appeared in
    n = [0,1]
    cur_n = 2
    while cur_n <= max_n:
        #print("cur_n is:", cur_n)
        #print("-----------------")
        #print()
        cur_seq = []
        seq_det = False
        val = cur_n
        while not seq_det:
            #print("val is:", val)
            if val < cur_n: #already found collatz seq
                #print("val<cur_n")
                cur_seq.extend(c[val])
                seq_det = True
            elif val in d:
                #print("val in d")
                index_of_seq_val_in = d[val]
                seq_val_in = c[index_of_seq_val_in]
                start_index = seq_val_in.index(val)
                cur_seq.extend(seq_val_in[start_index:])
                seq_det = True
            else:
                d[val] = cur_n
                cur_seq.append(val)
                val = collatz(val)
  
            #print("cur_seq is", cur_seq)
            #print("d is:", d)
            #print()
             
        c.append(cur_seq)
        n.append(len(cur_seq))
        #print("n[",cur_n,"] is:", n[cur_n])
        cur_n += 1
        #print()
        #print()

    return c,n
 
if __name__ == '__main__':   
    start = time.time()
    
    n = 1000000
    my_c, my_n = build_collatz(n)
    max_len = max(my_n)
    index_of_max = my_n.index(max_len)

    end = time.time()
    
    print("max length is", max_len)
    print("index of max is:", index_of_max)
    print("Took", end-start, "seconds")
    
    #print(collatz(3))
    #print(collatz_seq(3))
    #Answer: 837799

