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
 which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
 So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import time

def get_name_score(value_dict, name, pos): #name a string
    name_chars = list(name) #e.g. takes 'ALEX' to ['A', 'L', 'E', 'X']
    pre_pos_score = 0
    for i in range(len(name_chars)):
        pre_pos_score += value_dict[name_chars[i]]
        
    return pos* pre_pos_score


def solution_1(name_file):
    
    names = sorted(name_file.readline().split(','))
    #print(names)
    letters_index = [i for i in range(1, 27)]
    letters = [chr(letters_index[i] + 64) for i in range(len(letters_index))]
    #print(letters)
    value_dict = {letters[i]:letters_index[i] for i in range(len(letters_index))}
    #print(value_dict)
  
    score = 0 #49, 70, 57 first three scores
    for i in range(1, len(names) + 1): 
        #names list of form ['"name1"', '"name2"', ... ] so need to remove the surrounding "'s
        cur_name = names[i-1].replace("\"", "")  #e.g. takes '"name1"' to 'name1'
        current_score = get_name_score(value_dict, cur_name, i)
        score += current_score
    
    return score


if __name__ == '__main__':
    
    name_file = open("p022_names.txt", "r")
    
    start = time.time()
    res_1 = solution_1(name_file)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))  
        
    name_file.close()
    
    # Answer: 871198282



