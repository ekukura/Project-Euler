#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:23:14 2017

@author: emilykukura

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

my notation implies pronunciation:
    4,213 -> 4 thousand, 2 hundred, and 13

"""

import math, time

# dictionaries mapping numbers to the length of their spellings,
# e.g. ones[2] = 3 because "two" has 3 letters
#    teens[13] = 8 b/c "thirteen" has 8 letters

# Note for my purpose, the 'teens' dict refers to all numbers between 10 and 19, 
# not just the literal 'teens' 13-19
ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
ten_mults = {20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}
qualifiers = {"hundred":7, "thousand":8, "and":3}

def solution_1(max_num): #only does up to 9999
    num_letters = 0
    
    if max_num < 0:
        print("invalid input")
        return None
    
    elif max_num == 0:
        pass
            
    elif max_num <= 9:
        for i in range(1, max_num + 1):
            num_letters += ones[i]
            
    else:
        num_ones = max_num % 10
        num_tens = int((max_num % 100 - num_ones)/10)
        num_hundreds = int((max_num % 1000 - 10*num_tens-num_ones)/100)
        num_thousands = int(math.floor(max_num / 1000))
        #print(num_ones, num_tens, num_hundreds, num_thousands)
        
        letters_per_ones_cycle = solution_1(9) #1-9
        
        if max_num >= 10 and max_num <= 19:
            num_letters = solution_1(9)
            for i in range(10, max_num + 1):
                num_letters += teens[i]
                
        
        elif max_num >= 20 and max_num <= 99:
            
            num_letters = solution_1(19)
            
            # process all but last [possibly incomplete] 'ten' cycle
            # 
            # for 2 to num_tens-1, have full cycle, so e.g. word "twenty" appears 10 times, in:
            # 'twenty', 'twenty one', 'twenty two', ... , 'twenty nine'
            # last ten cycle to be processed seperately since it may be incomplete, e.g.
            # in the case of max_num = 35
            
            for i in range(2, num_tens): 
                num_letters += 10*ten_mults[10*i]          
                
            num_letters += (num_tens - 2) * letters_per_ones_cycle #e.g. if 35, so num_tens = 3, need
                                    #only to count ones cycle from 21-29 (first 1-9 already accounted
                                    #for, and 10-19 don't their own special spelling which have already
                                    #been accounted for)
            #process last 'ten'
            num_letters += (num_ones + 1) * ten_mults[10*num_tens] # e.g. if 35, add "thirty" 5+1 = 6 times
            num_letters += solution_1(num_ones)


        else:
            letters_per_tens_cycle = solution_1(99) #1-99
            
            if max_num >= 100 and max_num <= 999:
                #max_num >= 100
                
                #process all but last 'hundred' 
                num_letters += (num_hundreds * letters_per_tens_cycle) 
                #below is for the number in the hundreds place, e.g.
                #in 201 counts the 'two' in 'two hundred and one'
                for i in range(1, num_hundreds): 
                    num_letters += 100*ones[i]
                #below counts the 'hundred and' in e.g. 'two hundred and one'
                num_letters += 100*(num_hundreds - 1)* qualifiers["hundred"]
                num_letters += 99*(num_hundreds - 1)* qualifiers["and"] #don't need add for "hundred"
                
                #process last 'hundred'  
                #e.g. if 356, process 'three hundred' 57 times, 'and' 56 times
                num_letters += ((max_num % 100) + 1) * (ones[num_hundreds] + qualifiers["hundred"])
                num_letters += (max_num % 100) * qualifiers["and"]
                
                #processes the '56' part of 356
                num_letters += solution_1(max_num % 100)
            
            
            else: #max_num >= 1000
                letters_per_hundreds_cycle = solution_1(999) #1-999
                
                #process all but last 'thousand' 
                num_letters += (num_thousands * letters_per_hundreds_cycle)
                for i in range(1, num_thousands):
                    num_letters += 1000 * ones[i]
                    
                num_letters += 1000 *(num_thousands - 1) * qualifiers["thousand"]
        
                #process last 'thousand' 
                num_letters += ((max_num % 1000) + 1) * (ones[num_thousands] + qualifiers["thousand"])
                num_letters += solution_1(max_num % 1000)
                

    return num_letters


if __name__ == '__main__':   
    
    #num = 5
    num = 1000
    

    start = time.time()
    res_1 = solution_1(num)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))  
  
    #Answer: 21124


