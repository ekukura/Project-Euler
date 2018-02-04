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

import math

#ten_mults = {"twenty":6, "thirty":6, "forty":5, "fifty":5, "sixty":5
#             "seventy":7, "eighty":6, "ninety":6}
#ones = {"one":3, "two":3, "three":5, "four":4, "five":4, "six":3, "seven":5, "eight":5, "nine":4}
#tens = {"ten":3, "eleven":6, "twelve":6, "thirteen":8, 
#        "fourteen":8, "fifteen":7, "sixteen":7, "seventeen":9, "eighteen":8, "nineteen":8 }


#print(3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4)
ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
ten_mults = {20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}
qualifiers = {"hundred":7, "thousand":8, "and":3}

def naive_letter_count(num_str):
    return len(num_str)

#print(naive_letter_count("ten"))

def letters(max_num): #only does up to 9999
    num_letters = 0
    
    if max_num == 0:
        return 0
            
    elif max_num <= 9:
        for i in range(1, max_num + 1):
            num_letters += ones[i]
    else:
        num_ones = max_num % 10
        num_tens = int((max_num % 100 - num_ones)/10)
        num_hundreds = int((max_num % 1000 - 10*num_tens-num_ones)/100)
        num_thousands = int(math.floor(max_num / 1000))
        
        letters_per_ones_cycle = letters(9) #1-9
        
        if max_num >= 10 and max_num <= 19:
            num_letters = letters(9)
            for i in range(10, max_num + 1):
                to_add = teens[i]
                num_letters += to_add
                #num_letters += teens[i]
                
            return num_letters
        
        elif max_num >= 20 and max_num <= 99:
            
            num_letters = letters(19)
            
            #process all but last 'ten'
            #for 2 to num_tens-1, have full cycle, so e.g. word "twenty" appears 10 times
            for i in range(2, num_tens): 
                num_letters += 10*ten_mults[10*i]          
                
            num_letters += (num_tens - 2) * letters_per_ones_cycle #e.g. if 35, so num_tens = 3, need
                                                       #to count ones cycle from 21-29 (already did first 1-9)
            #process last 'ten'
            num_letters += (num_ones + 1) * ten_mults[10*num_tens] # e.g. if 35, add "thirty" 5+1 = 6 times
            num_letters += letters(num_ones)
            
            return num_letters  

        else:
            letters_per_tens_cycle = letters(99) #1-99
            
            if max_num >= 100 and max_num <= 999:
                #max_num >= 100
                
                #process all but last 'hundred' 
                num_letters += (num_hundreds * letters_per_tens_cycle) 
                for i in range(1, num_hundreds): 
                    num_letters += 100*ones[i]
                
                num_letters += 100*(num_hundreds - 1)* qualifiers["hundred"]
                num_letters += 99*(num_hundreds - 1)* qualifiers["and"] #don't need add for "hundred"
                
                #process last 'hundred'  
                #e.g. if 356, process three hundred 57 times
                num_letters += ((max_num % 100) + 1) * (ones[num_hundreds] + qualifiers["hundred"])
                num_letters += (max_num % 100) * qualifiers["and"]
                
                num_letters += letters(max_num % 100)
            
                return num_letters
            
            else: #max_num >= 1000
                letters_per_hundreds_cycle = letters(999) #1-999
                
                #process all but last 'thousand' 
                num_letters += (num_thousands * letters_per_hundreds_cycle)
                for i in range(1, num_thousands):
                    num_letters += 1000 * ones[i]
                    
                num_letters += 1000 *(num_thousands - 1) * qualifiers["thousand"]
        
                #process last 'thousand' 
                num_letters += ((max_num % 1000) + 1) * (ones[num_thousands] + qualifiers["thousand"])
                num_letters += letters(max_num % 1000)
                
                return num_letters
        #return(num_ones, num_tens, num_hundreds, num_thousands)
          
    return num_letters

#print(letters(100))
#1-9 
#print(letters(9)) letters(9) = 36
#print(letters(99))

#for i in range(9,100):
#    print("i = ", i, "letters = ", letters(i))
    
#print(letters(10))

#print(letters(5))
#print(letters(4231))
print(letters(1000)) #21044
#need 'ands' still