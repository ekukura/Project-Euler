#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:29:59 2017

@author: emilykukura

By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23 = 3 + 7 + 4 + 9 .

3
7 4
2 4 6
8 5 9 3


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

my_triangle = [[75], 
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
            for i in range(cur_row_index + 1):
                if i == 0:
                    before_set = prev_row[0]
                elif i == cur_row_index:
                    before_set = prev_row[cur_row_index - 1]
                else:
                    #print("prev_row[i - 1] = ", prev_row[i - 1])
                    #print("prev_row[i] = ", prev_row[i])
                    before_set = set.union(prev_row[i - 1], prev_row[i])
                
                #print("i = ", i)
                #print("before_set = ", before_set)
                cur_row.append({ j + triangle[cur_row_index][i] for j in before_set})
            
            #print("cur_row = ", cur_row)
            path_sums.append(cur_row)
            #print("path_sums = \n", path_sums)
            cur_row_index += 1
            
        return path_sums

def get_max_sum_brute(triangle):
    all_sums = get_all_sums(triangle)
    rel_sums = all_sums[len(triangle) - 1]
    candidates = set()
    #print(rel_sums)
    for i in range(len(rel_sums)):
        candidates = set.union(candidates, rel_sums[i])
    print("there are", len(candidates), "candidates")
    return max(candidates)
    

def get_max_sum_recursive2(triangle):
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
        #print(triangle)
        #print("prev_triangle = ", prev_triangle)
        prev_max_sums = get_max_sum_recursive2(prev_triangle)[1]
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
    
    #print("new_max_sums = ", new_max_sums)
    #print("max_sum = ", max_sum)
        
    return [max_sum , new_max_sums]
   
def get_max_sum_recursive(triangle):
    num_rows = len(triangle)
    if num_rows < 1:
        return None
    elif num_rows == 1:
        new_max_sums = triangle[0]
    else:
        prev_triangle = list(triangle)
        prev_triangle.pop()
        prev_max_sums = get_max_sum_recursive(prev_triangle)
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
  
def get_max_sum_dyn(triangle):
    num_rows = len(triangle)
    if num_rows < 1:
        return None
    else:
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
        my_max = max([max(max_sums[i]) for i in range(len(max_sums))])
        
    return max_sums, my_max

#for i in range(len(triangle)):
#    print(triangle[i])
#test_triangle = []
#for i in range(4):
#    test_triangle.append(my_triangle[i])
    

'''
num_rows = 5
a = [np.random.randint(1, high = 10, size = (i)) for i in range(1,num_rows + 1) ]
for i in range(len(a)):
    print(a[i])
print()
res, amax = get_max_sum_dyn(a)
print()
for i in range(len(res)):
    print(res[i])
print()
print(amax)
'''



#'''
print()
start = time.time()
res = max(get_max_sum_recursive(my_triangle))
end = time.time()
print("res = ", res)
print("took", end-start, "seconds")

start2 = time.time()
res2 = get_max_sum_recursive2(my_triangle)[0]
end2 = time.time()
print("res2 = ", res2)
print("took", end2-start2, "seconds")

start3 = time.time()
res3 = get_max_sum_brute(my_triangle)
end3 = time.time()
print("res3 = ", res3)
print("took", end3-start3, "seconds")

start4 = time.time()
sums, res4 = get_max_sum_dyn(my_triangle)
end4 = time.time()
print("res4 = ", res4)
print("took", end4-start4, "seconds")
#'''

#print("a[0][0] = ", a[0][0])

#sums = get_all_sums(test_triangle)
#print("sums = ", sums)
#print(len(sums))
#for i in range(len(sums)):
#    print(sums[i])


#print()
#res = get_max_sum_brute(my_triangle)
#print(res)

#print()


'''   
a = {0}
b = {1,2}
c = {3,4}

print([[a]])
my_l = [[a], [b,c]]
print(my_l)

b = set()
b.add(4)
b.add(3)
print(b)

b = [[6], [3,8], [1,5,2]]
c = [max(b[i]) for i in range(len(b))]
d = max([max(b[i]) for i in range(len(b))])
print(c)
print(d)
#'''

#print(test_triangle)
