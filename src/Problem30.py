'''
Created on May 11, 2018

@author: emilykukura

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4  ( = 1 + 1296 + 81 + 256 = 1297 + 337 = 1500 + 97 + 37 = 1634 )
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Answer:
443839
'''
import math, time

def sum_pow(num, p):
    '''
    sums the p-the powers of the digits of num
    
    Letting n = num_digits(num), this function is O(n)
    '''
    num_str = str(num)
    digits = [int(num_str[i]) for i in range(len(num_str))]
    power_digits = [pow(d,p) for d in digits]
    #print(digits)
    #print(power_digits)
    return sum(power_digits)


def get_satisfying_n_digit_numbers_brute(num_digits,p):
    '''
    Letting n = num_digits, this method returns all numbers x s.t. x = sum_pow(x,p)
    
    Since there are O(10^n) integers with n digits, and for each sum_pow is calculated
    in O(n) time, this method runs in O(n*10^n) time 
    '''
    min_cand = pow(10, num_digits-1)
    max_cand = pow(10, num_digits) - 1
    satisfying_nums = []
    for cand in range(min_cand, max_cand + 1):
        cur_sum = sum_pow(cand,p)
        if cur_sum == cand:
            satisfying_nums.append(cur_sum)
    
    return satisfying_nums


def get_highest_num_digits(p):
    '''
    :type p: int
    Let f(p) = 10^(ceil(log10(p))) - (ceil(log10(p)+1)
    Then if p < f(p), will have that x > sum_pow(x,p) for all m = num_digits s.t.
        m >= (p+1) + ceil(log10(p))
    else,  x > sum_pow(x,p) for all m = num_digits s.t.
        m >= (p+2) + ceil(log10(p))
        
    '''  
    f = pow(10, math.ceil(math.log10(p))) - (math.ceil(math.log10(p)) + 1)
    if p < f:
        max_digits = p + math.ceil(math.log10(p))
    else:
        max_digits = p + 1 + math.ceil(math.log10(p))
   
    return  max_digits



def solution_1(p):
    '''
    At some point numbers too big to possibly satisfy this criteria.
    For a given number x, let n(x) = len(x) = # digits in x. 
    Let sum_pow(x,p) be the sum of the p-th powers of the digits in x. Then:
    --> Thus sum_pow(x,p) <= n(x)*(9^p) = (9^p)*n(x). 
    --> Note: n(a) > n(b) -> a > b
    -->        So, if n(x) > n( 9^p*n(x) ), then x > (9^p)*n(x) >= sum_pow(x,p), so that
    -->        x not equal to sum_pow(x,p)
    

    Let f(p) = 10^(ceil(log10(p)) - (ceil(log10(p)) + 1).
    There are two cases:
        (Case 1) p < f(p)
        (Case 2) p >= f(p)
        
    I claim that in case (1), n(x) > n( (9^p)*n(x) ) whenever n(x) >= (p+1) + ceil(log10(p))
            while in case (2), n(x) > n( (9^p)*n(x) ) whenever n(x) >= (p+2) + ceil(log10(p))
   
    For example, for p = 4, this holds for n(x) >= 6, since 4 = p < f(p) = 10^(1) - (2) = 8:

    To prove the special case p = 4 we have:
        sum_pow(x,4) <= (9^4)*n(x) < 10^4 * n(x) = 10^(4 + log10(n(x))
        -> n(sum_pow(x,4)) <= n( (9^4)*n(x) ) < 5 + log10(n(x))
        AND  5 + log10(n(x)) < n(x) IFF 10^5*n(x) < 10^n(x) IFF n(x) < 10^(n(x) - 5)
        IFF n(x) >= 6
        
        And to prove  n(x) < 10^(n(x) - 5) IFF n(x) >= 6 we have:
        Base (n(x) = 6): 6 < 10^(6-5) = 10
        Inductive (n(x) < 10^(n(x)-5) -> n(x)+1 < 10^(n(x)+1-5) :  
            Assume n(x) < 10^(n(x)-5): Then since for all r>=1, r+1 <= 10*r, and since 
                10^(n(x)-5) >= 10 (since n(x)>=6):
                -> (n(x)+1) < 10^(n(x)-5) + 1 < 10*(10^(n(x)-5)) = 10^(n(x)-4) = 10^((n(x)+1) - 5).
                Done.   
        Thus we only need to check for x s.t. 2 <= n(x) <= 5 when p = 4
      
      
    For General x and p a fixed positive integer:
        (9^p)*n(x) < 10^p * n(x) = 10^(p + log10(n(x))
        -> log10( (9^p)*n(x)  ) < p + log10(n(x))
    AND ALSO  note that n(x) = floor( log10(x)) + 1
    
    Thus:
        floor( log10( (9^p)*n(x))) + 1 < floor( p + log10(n(x))) + 1 = (p+1) + floor(log10(n(x))
    ->     n(sum_pow(x,p)) <= n( (9^p)*n(x) ) < (p+1) + log10(n(x)). 
        Thus for any x s.t. (p+1) + log10(n(x)) < n(x), we have  n(sum_pow(x,p)) < n(x) 
            and thus sum_pow(x,p) < x
        
    So it suffices to show that:
        (Case 1) When p < f(p),  (p+1) + log10(n(x)) < n(x) for all n(x) >= (p+1) + ceil(log10(p))       
        (Case 2) When p >= f(p),  (p+1) + log10(n(x)) < n(x) for all n(x) >= (p+2) + ceil(log10(p))         

    Let m = n(x), so that we want to show (p+1) + log10(m) < m for m sufficiently large.
    
    
    **Proof**: First note that the following statements are equivalent:
    
        - (p+1) + log10(m) < m  
        - 10^((p+1) + log10(m)) < 10^m  
        - (10^(p+1))*m < 10^m
        - m < 10^(m-(p+1))
            
        This it suffices to show that for all m sufficiently large, 
            m < 10^(m-(p+1)), which we will show by induction for both of the two cases:
        
        Case 1: p < f(p) = 10^(ceil(log10(p)) - (ceil(log10(p)) + 1)
        
        Base (m = (p+1) + ceil(log10(p))):
            Since p < f(p): 
            m = (p+1) + ceil(log10(p)) 
                < 10^(ceil(log10(p)) - (ceil(log10(p)) + 1) + 1 + ceil(log10(p))
                = 10^(ceil(log10(p)) 
                = 10 ^ ( (p+1) + ceil(log10(p)) - (p+1) ) 
                = 10^(m-(p+1)). Done.
            
        Then inductively: Assume m < 10^(m-(p+1)) for a fixed p.
            (m+1) < 10^(m-(p+1)) + 1 
                < 10*10^(m-(p+1))  (since for all r>=1, r+1 <= 10*r, and 10^(m-(p+1)) >= 1 since m > (p+1))
                = 10^((m+1) - (p+1)). Done.
                
        Note this inductive argument will be the same for Case 2 as well, and so all that
        is left is proving the base case for Case 2,
        when p >= f(p) = 10^(ceil(log10(p)) - (ceil(log10(p)) + 1):
        
        Base (m = (p+2) + ceil(log10(p))):
            m = (p+2) + ceil(log10(p)) 
              < (p+3) + log10(p) 
              < (p+3) + p = 2*p + 3
              < 10 * p (since p >= 1)
              = 10 * 10^(log10(p))
              < 10 * 10^(ceil(log10(p))
              = 10 ^ (1 + ceil(log10(p)) ) 
              = 10 ^ ( (p+2) + ceil(log10(p)) - (p+1) ) 
              = 10^(m-(p+1)). Done.
                 
    '''
    
    max_digits = get_highest_num_digits(p) #e.g. max_digits = 5 when p = 4
    satisfying_numbers = []
    for num_digits in range(2, max_digits + 1):
        #find all x s.t. n(x) = num_digits and x = sum_four(x)
        satisfying_numbers.extend(get_satisfying_n_digit_numbers_brute(num_digits, p))
    
    print(satisfying_numbers)
    res = sum(satisfying_numbers)
    
    return res


if __name__ == '__main__':

    '''
    #testing supplementary methods:
    
    r = get_highest_num_digits(995)
    #print(r)

    for x in [1634, 8208, 9474]:
        r = sum_pow(x,4)
        #print(r)
        assert(r == x)
        
    #print(2*pow(10,2) + 3*pow(10,3) + 4*pow(10,4) + 5*pow(10,5))
    
    ns = get_satisfying_n_digit_numbers_brute(4, 4)
    print(ns)
        
    #res = solution_1()
    #print(res)
    #'''
    
    p = 5
    start = time.time()
    res_1 = solution_1(p)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))    
    
    #Answer: 443839
