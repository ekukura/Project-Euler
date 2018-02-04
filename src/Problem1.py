'''
Created on Feb 3, 2018

@author: emilykukura
'''

#Answer: 233168

'''
If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import math, time

#add sum of multiples of 3 and sum of multiples of 5, subtract 
#multiples of 15

#the sum of all multiples of k <= N is 
#sum([k*i for i in range(1,floor(N-1/k))] 
# = k*sum(i for i in range(1,floor(N/k)) = k*(floor(N/k)*(floor(N/k) + 1)/2

#cum_sum(n) returns sum of integers from 1 to n
def cum_sum(max_num):
    return max_num*(max_num+1)/2

def get_multiples_sum(factor, N):    
    return factor*cum_sum(math.floor((N)/factor))

if __name__ == '__main__':
    #testing...
    print(cum_sum(3))
    M = 1000
    start = time.time()
    first_sum = get_multiples_sum(3, M-1)
    second_sum = get_multiples_sum(5, M-1)
    cross_sum = get_multiples_sum(15, M-1)
    res = first_sum + second_sum - cross_sum
    end = time.time()
    print("res = ", res)
    print("Computed in:", end-start)
    