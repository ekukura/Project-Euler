#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:18:03 2017

@author: emilykukura

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

-Jan 1 1901 a Tuesday
-> Jan 6 1901 a Sunday
"""

import time

def count_first_sundays():
    count = 0
    
    regular_year_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 
                             8:31, 9:30, 10:31, 11:30, 12:31}
    
    leap_year_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 
                             8:31, 9:30, 10:31, 11:30, 12:31}
    
    day = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, 
                "Thursday":4, "Friday":5, "Saturday":6}
    
    start_day = day["Tuesday"]
    curr_day = start_day
    
    ## loop through the "1sts" of every year. If a Sunday, add 1 to count
    for year in range(1901, 2001):
        #print("\n\nyear is:", year)
        if (year % 4 == 0) and ((not year % 100 == 0) or year % 400 == 0): #is a leap year
            days_per_month = leap_year_days
        else: #not a leap year
            days_per_month = regular_year_days
            
        for month in range(1,13):
            #print("\nmonth is", month)
            #print("curr_day is", curr_day)
            if curr_day == 0: #0 corresponds to "Sunday" in day dict
                count += 1          
        
            #print("count is:", count)
            curr_day = (curr_day + days_per_month[month]) % 7
        
    return count

def solution_1():
    return count_first_sundays()

if __name__ == '__main__':   
    
    start = time.time()
    res_1 = solution_1()
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))  

    # Answer: 171

