#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:29:59 2017

@author: emilykukura

By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 
23 = 3 + 7 + 4 + 9 .

    3
   7 4
  2 4 6
 8 5 9 3

Find the maximum total from top to bottom of the triangle below:

                        75
                      95 64
                     17 47 82
                   18 35 87 10
                  20 04 82 47 65
                19 01 23 75 03 34
               88 02 77 73 07 63 67
             99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
         53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
   
"""

import numpy as np
import time

def get_all_sums(triangle):
    
    num_rows = len(triangle)
    if num_rows < 1:
        return None
    elif num_rows == 1:
        return {triangle[0][0]}
    else:
        
        path_sums = [[{triangle[0][0]}]] 
        cur_row_index = 1
        
        while cur_row_index < len(triangle):
            #print("cur_row_index = ", cur_row_index)
            prev_row = path_sums[cur_row_index - 1]
            cur_row = []

            for i in range(cur_row_index + 1): #i corresponds to the column index
                #the before_set variable below will contain all possible path sums ending in location
                #(row, col) = (cur_row_index, i) BEFORE the element in column i is added
                if i == 0: #if in first column, path must go through previous row's first element
                    before_set = prev_row[0]
                elif i == cur_row_index: #if in last column, path must go through previous row's last element
                    before_set = prev_row[cur_row_index - 1]
                else: #if not in first or last column, path can go through either the element to upper left or upper right
                    before_set = set.union(prev_row[i - 1], prev_row[i])
                
                final_element = triangle[cur_row_index][i]
                cur_row.append({ j + final_element for j in before_set})
            
            #print("cur_row = ", cur_row)
            path_sums.append(cur_row)
            #print("path_sums = \n", path_sums)
            cur_row_index += 1
            
        return path_sums

def get_max_sum_brute(triangle):
    all_sums = get_all_sums(triangle)
    rel_sums = all_sums[len(triangle) - 1] #only last row matters
    candidates = set()
    #print(rel_sums)
    for i in range(len(rel_sums)):
        candidates = set.union(candidates, rel_sums[i])
    #print("there are", len(candidates), "candidates")
    return max(candidates)
   
def get_max_sums_recursive(triangle):
    num_rows = len(triangle)
    if num_rows < 1:
        return None
    elif num_rows == 1:
        new_max_sums = triangle[0]
    else:
        prev_triangle = list(triangle)
        prev_triangle.pop() #prev_triangle is triangle without its last row
        prev_max_sums = get_max_sums_recursive(prev_triangle)
        #prev_max_sums is an array of length equal to the length
        #of prev_triangle. it's i-th element is the maximum sum which ends
        #in the i-th column of the last row of prev_triangle 
        new_max_sums = []
        for i in range(num_rows): #note num_rows is the same as num elements in last row
            if i == 0:
                new_max = prev_max_sums[i] + triangle[num_rows-1][i]
            elif i == num_rows - 1:
                new_max = prev_max_sums[i-1] + triangle[num_rows-1][i]
            else:
                prior_max = max(prev_max_sums[i-1], prev_max_sums[i])
                new_max= prior_max + triangle[num_rows-1][i]
            new_max_sums.append(new_max)
        
    return new_max_sums
      

# same as get_max_sums_recursive except also keeps track of the absolute
# maximum sum, not only the entire row of maximum sums ending at each location
# in the final row
def get_max_sums_recursive2(triangle):
    num_rows = len(triangle)
    #print("num_rows = ", num_rows)
    if num_rows < 1:
        return None
    elif num_rows == 1:
        max_sum = triangle[0][0]
        new_max_sums = triangle[0]
    else:
        prev_triangle = list(triangle)
        prev_triangle.pop()
        prev_max_sums = get_max_sums_recursive2(prev_triangle)[1]
        #print("prev_max_sums = ", prev_max_sums)
        new_max_sums = []
        for i in range(num_rows): #note num_rows is the same as num elements in last row
            if i == 0:
                new_max = prev_max_sums[i] + triangle[num_rows-1][i]
            elif i == num_rows - 1:
                new_max = prev_max_sums[i-1] + triangle[num_rows-1][i]
            else:
                prior_max = max(prev_max_sums[i-1], prev_max_sums[i])
                new_max= prior_max + triangle[num_rows-1][i]
            #print("new_max = ", new_max)
            new_max_sums.append(new_max)
            
        max_sum = max(new_max_sums)
        
    return [max_sum , new_max_sums]

#operates essentially the same as get_max_sums_recursive except
#with a dynamic build-up instead of a recursive method
def get_max_sum_dyn(triangle):
    num_rows = len(triangle)
    if num_rows < 1:
        return None
    else:
        #max_sums now will end up of same shape as triangle, and
        #the (i,j)-th element will be the maximum sum of a path ending
        #in the (i,j)-th element of the triangle
        max_sums = [triangle[0]]
        for row_index in range(1,len(triangle)):
            prev_sums = max_sums[row_index - 1]
            new_sums = []
            for col_index in range(row_index + 1):
                if col_index == 0:
                    new_max = prev_sums[col_index] + triangle[row_index][col_index]
                elif col_index == row_index:
                    new_max = prev_sums[col_index-1] + triangle[row_index][col_index]
                else:
                    prior_max = max(prev_sums[col_index-1], prev_sums[col_index])
                    new_max= prior_max + triangle[row_index][col_index]
                new_sums.append(new_max)           
            max_sums.append(new_sums)          
        my_max = max(max_sums[num_rows-1]) #just look at last row
        #print(max_sums)
        
    return max_sums, my_max


def solution_1(my_triangle):
    return max(get_max_sums_recursive(my_triangle))

def solution_2(my_triangle):
    return get_max_sums_recursive2(my_triangle)[0]

def solution_3(my_triangle):
    return get_max_sum_brute(my_triangle)

def solution_4(my_triangle):
    return get_max_sum_dyn(my_triangle)

if __name__ == '__main__':   

    
    test_triangle = [
            [3],
            [7,4],
            [2,4,6],
            [8,5,9,3]
            ]
    
    #print(get_all_sums(test_triangle))
    #print(get_max_sum_brute(test_triangle))
 
    my_triangle = [
            [75], 
            [95,64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
            ]
    

    start = time.time()
    res_1 = solution_1(my_triangle)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start)) 
    
    start = time.time()
    res_2 = solution_2(my_triangle)
    end = time.time()
    print("res_2 = {}\nTook {} seconds".format(res_2, end-start))  

    start = time.time()
    res_3  = solution_3(my_triangle)
    end = time.time()
    print("res_3 = {}\nTook {} seconds".format(res_3, end-start)) 
    
    start = time.time()
    sums, res_4 = solution_4(my_triangle)
    end = time.time()
    print("res_4 = {}\nTook {} seconds".format(res_4, end-start))  
    #print("sums = {}".format(sums))
           
    # Answer: 1074

