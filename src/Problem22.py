#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:09:36 2017

@author: emilykukura

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
 which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

import time

name_file = open("p022_names.txt", "r")

names = sorted(name_file.readline().split(','))
num_names = len(names)

letters_num = [i for i in range(1,27)]
letters = [chr(letters_num[i] + 64) for i in range(len(letters_num))]
#print(letters)
value_dict = {letters[i]:letters_num[i] for i in range(len(letters_num))}
print(value_dict)
print()

def get_name_score(name, pos): #name a string
    name_chars = list(name)
    #print(name_chars)
    score = 0
    for i in range(len(name_chars)):
        score += pos * value_dict[name_chars[i]]
        #print(score)
        
    return score

start = time.time()
score = 0 #49, 70, 57 first three scores
for i in range(len(names)):
#for i in range(3):
    cur_name = names[i].replace("\"","")
    current_score = get_name_score(cur_name, i+1)
    score += current_score

res = score
end = time.time()
print("The total score is:", score)
print("Took {} seconds".format(end-start))



'''
name = names[0]
print(list(name.replace("\"", "")))
print(name)
name_chars = list(name)
print(name_chars)
print(num_names)
print(names[0])
print(names[0][1])
print(ord(names[0][1]))
print(names[num_names - 1])
print(names[937])
'''

name_file.close()