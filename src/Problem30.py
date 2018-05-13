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
import math, time, itertools

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
    

    Let f(p) = 10^(ceil(log10(p)) - ceil(log10(p)).
    There are two cases:
        (Case 1) p < f(p)
        (Case 2) p >= f(p)
        
    I claim that in case (1), n(x) > n( (9^p)*n(x) ) whenever n(x) >= (p+1) + ceil(log10(p))
            while in case (2), n(x) > n( (9^p)*n(x) ) whenever n(x) >= (p+2) + ceil(log10(p))
   
    For example, for p = 4, this holds for n(x) >= 6, since 4 = p < f(p) = 10^(1) - (1) = 9:

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
        Thus for any x s.t. (p+1) + log10(n(x)) <= n(x), we have  n(sum_pow(x,p)) < n(x) 
            and thus sum_pow(x,p) < x
        
    So it suffices to show that:
        (Case 1) When p < f(p),  (p+1) + log10(n(x)) <= n(x) for all n(x) >= (p+1) + ceil(log10(p))       
        (Case 2) When p >= f(p),  (p+1) + log10(n(x)) <= n(x) for all n(x) >= (p+2) + ceil(log10(p))         

    Let m = n(x), so that we want to show (p+1) + log10(m) <= m for m sufficiently large.
    
    
    **Proof**: First note that the following statements are equivalent:
    
        - (p+1) + log10(m) <= m  
        - 10^((p+1) + log10(m)) <= 10^m  
        - (10^(p+1))*m <= 10^m
        - m <= 10^(m-(p+1))
            
        This it suffices to show that for all m sufficiently large, 
            m <= 10^(m-(p+1)), which we will show by induction for both of the two cases:
        
        Case 1: p < f(p) = 10^(ceil(log10(p)) - ceil(log10(p)) 
            *Note since f(p) is an integer, this means p+1 <= f(p)
        
        Base (m = (p+1) + ceil(log10(p))):
            Since p+1 <= f(p): 
            m = (p+1) + ceil(log10(p)) 
                <= f(p) + ceil(log10(p))
                = 10^(ceil(log10(p)) - ceil(log10(p)) + ceil(log10(p))
                = 10^(ceil(log10(p)) 
                = 10 ^ ( (p+1) + ceil(log10(p)) - (p+1) ) 
                = 10^(m-(p+1)). Done.
            
        Then inductively: Assume m <= 10^(m-(p+1)) for a fixed p.
            (m+1) <= 10^(m-(p+1)) + 1 
                <= 10*10^(m-(p+1))  (since for all r>=1, r+1 <= 10*r, and 10^(m-(p+1)) >= 1 since m > (p+1))
                = 10^((m+1) - (p+1)). Done.
                
        Note this inductive argument will be the same for Case 2 as well, and so all that
        is left is proving the base case for Case 2,
        when p >= f(p) = 10^(ceil(log10(p)) - (ceil(log10(p))):
        
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


def get_nums_with_max_digit_mag(n, max_digit_mag):
    '''
    :returns: any <= n digit numbers whose digits are all <= max_digit_mag in magnitude
    '''
    list_nums = [ list(v) for v in itertools.product(range(max_digit_mag + 1), repeat = n)]
    vals = [sum(pow(10,i) * list_num[i] for i in range(n)) for list_num in list_nums]
   
    return vals


def get_n_digit_nums_with_max_digit_mag(n, max_digit_mag):
    
    remainders = get_nums_with_max_digit_mag(n-1, max_digit_mag)
    vals = []
    for first_digit in range(1, max_digit_mag + 1):
        #here we need to generate all n-digit numbers starting with first_digit
        # should be ((max_mag)+1)^(n-1) such numbers
        vals.extend([pow(10,n-1)*first_digit + r for r in remainders])            
    
    return vals


def get_satisfying_n_digit_numbers_mag(n,p):
    '''
    Dealing with n-digit numbers, power-p sums.
    If any digit has value >= log_p(10^n), then will have x < sum_pow(x,p)
    '''
    satisfying_nums = []
    max_digit_mag = math.ceil(math.pow(math.pow(10,n), 1/p)) - 1
    #print("For n = {}, p = {}, the max_digit_mag is {}".format(n,p,max_digit_mag))
    
    #e.g. for n = 2, p = 5, want only digits with mag <= 2 (10, 11, 12, 20, 21, 22)
    
    if max_digit_mag < 9:
        candidates = get_n_digit_nums_with_max_digit_mag(n, max_digit_mag)
    else:
        candidates = [val for val in range(pow(10, n-1), pow(10, n) - 1)]
        
    for cand in candidates:
        cur_sum = sum_pow(cand,p)
        if cur_sum == cand:
            satisfying_nums.append(cur_sum)
    
    return satisfying_nums


def solution_2(p):
    '''
    In solution_1, we found an upper bound on the digit-length of a feasible candidate, 
    which depended on the value of p (e.g. when p = 5, only need to consider
    x with no more than 6 digits
    
    Now, for each digit length, we can use p also to determine an upper bound on the 
    magnitude of feasible candidates. 
    
    Let di = di(x) be the digit of x in the i-th place, e.g. if x = 534, then
    d2 = 5, d1 = 3, and d0 = 4.
    
    Then since always x < 10^(n(x)), if di^p >= 10^(n(x)) for any di, then 
    x < di^p < sum_pow(x,p).
    
    For example, when p = 5:
        When n(x) = 2 we have that x < 100 for all x, and so there is no need 
            to consider any 2-digit number with a digit of magnitude >= 3,
            since 3^5 = 243 > 99.
        When n(x) = 3, x < 1000 for all x, and so no need to consider any 
            3-digit number with a digit of magnitude >= 5, since 5^5 = 3125 > 999
        When n(x) = 4, x < 10^4 for all x, and so no need to consider any 
            3-digit number with a digit of magnitude >= 7, since 5^7 = 16807 > 9999
            
    '''
    max_digits = get_highest_num_digits(p) #e.g. max_digits = 5 when p = 4
    satisfying_numbers = []
    for num_digits in range(2, max_digits + 1):
        #find all x s.t. n(x) = num_digits and x = sum_four(x)
        cur_values = get_satisfying_n_digit_numbers_mag(num_digits, p)
        satisfying_numbers.extend(cur_values)
        #print("For {}-digit numbers, found {}\n".format(num_digits, cur_values))
      
    print(satisfying_numbers)
    res = sum(satisfying_numbers)
    
    return res

def sum_pow_dict(num, p, p_powers):
    '''
    sums the p-the powers of the digits of num
    
    Letting n = num_digits(num), this function is O(n)
    '''
    num_str = str(num)
    digits = [int(num_str[i]) for i in range(len(num_str))]
    power_digits = [p_powers[d] for d in digits]
    #print(digits)
    #print(power_digits)
    return sum(power_digits)

def get_satisfying_n_digit_numbers_mag_dict(n,p,p_powers):
    '''
    Dealing with n-digit numbers, power-p sums.
    If any digit has value >= log_p(10^n), then will have x < sum_pow(x,p)
    '''
    satisfying_nums = []
    max_digit_mag = math.ceil(math.pow(math.pow(10,n), 1/p)) - 1
    #print("For n = {}, p = {}, the max_digit_mag is {}".format(n,p,max_digit_mag))
    
    #e.g. for n = 2, p = 5, want only digits with mag <= 2 (10, 11, 12, 20, 21, 22)
    
    if max_digit_mag < 9:
        candidates = get_n_digit_nums_with_max_digit_mag(n, max_digit_mag)
    else:
        candidates = [val for val in range(pow(10, n-1), pow(10, n) - 1)]
        
    for cand in candidates:
        cur_sum = sum_pow_dict(cand,p,p_powers)
        if cur_sum == cand:
            satisfying_nums.append(cur_sum)
    
    return satisfying_nums


def solution_3(p): 
    '''
    Same as soultion_2, but store all p-powers so don't have 
    to continuously compute
    '''
    p_powers = [pow(k,p) for k in range(10)]
    max_digits = get_highest_num_digits(p) #e.g. max_digits = 5 when p = 4
    satisfying_numbers = []
    for num_digits in range(2, max_digits + 1):
        #find all x s.t. n(x) = num_digits and x = sum_four(x)
        cur_values = get_satisfying_n_digit_numbers_mag_dict(num_digits, p, p_powers)
        satisfying_numbers.extend(cur_values)
        #print("For {}-digit numbers, found {}\n".format(num_digits, cur_values))
      
    print(satisfying_numbers)
    res = sum(satisfying_numbers)
    return res
    

def get_satisfying_n_digit_numbers_4(n, p, p_powers):
    '''
    Explanation...
    '''
    satisfying_nums = [] 
    max_digit_mag = min(math.ceil(math.pow(math.pow(10,n), 1/p)) - 1,9) 
  
    #so maximum first digit is max_digit_mag
    for first_digit in range(1, max_digit_mag + 1):
        upper_bound = pow(10, n-1)*(first_digit + 1) #any number with this first digit is smaller than this
        max_remaining_mag = math.ceil(pow(upper_bound, 1/p)) - 1 
        if max_remaining_mag < 9: 
            remainders = get_nums_with_max_digit_mag(n-1, max_remaining_mag)
            #print("for n = {}, p = {}, and first_digit = {}, ".format(n,p,first_digit) + 
            #      "max_rem_mag = {}".format(max_remaining_mag))
            #and remainders is: {}\n".format(remainders))
                
            for cur_rem in remainders:
                cand = pow(10,n-1)*first_digit + cur_rem
                cur_sum = sum_pow_dict(cand,p,p_powers)
                if cur_sum == cand:
                    satisfying_nums.append(cur_sum)
            
        else: #no need to check with original limit (max_digit_mag) 
                # -- if no limit here then this limit was also >= 9
                # so check all numbers
            for cur_rem in range(pow(10, n-2), pow(10, n-1) - 1):
                cand = pow(10,n-1)*first_digit + cur_rem
                cur_sum = sum_pow_dict(cand,p,p_powers)
                if cur_sum == cand:
                    satisfying_nums.append(cur_sum)

   
    return satisfying_nums


def solution_4(p): 
    '''  
    TODO: Add Description...
    '''
    p_powers = [pow(k,p) for k in range(10)]
    #print("leading terms:", leading_terms)
    max_digits = get_highest_num_digits(p) #e.g. max_digits = 5 when p = 4
    satisfying_numbers = []
    for num_digits in range(2, max_digits + 1):
        #find all x s.t. n(x) = num_digits and x = sum_four(x)
        cur_values = get_satisfying_n_digit_numbers_4(num_digits, p, p_powers)
        satisfying_numbers.extend(cur_values)
        #print("For {}-digit numbers, found {}\n".format(num_digits, cur_values))
      
    print(satisfying_numbers)
    res = sum(satisfying_numbers)
    
    return res

def get_satisfying_n_digit_numbers_5(n, p, p_powers):
    '''
    Explanation...
    '''
    satisfying_nums = [] 
    #max_digit_mag = min(math.ceil(math.pow(math.pow(10,n), 1/p)) - 1,9) 
    max_first_digit_mag = min(math.floor(n*pow(9,p)/pow(10,n-1)),9)

    for first_digit in range(1, max_first_digit_mag + 1):
        upper_bound = pow(10, n-1)*(first_digit + 1) #any number with this first digit is smaller than this
        max_remaining_mag = math.ceil(pow(upper_bound, 1/p)) - 1 
        if max_remaining_mag < 9: 
            remainders = get_nums_with_max_digit_mag(n-1, max_remaining_mag)
            #print("for n = {}, p = {}, and first_digit = {}, ".format(n,p,first_digit) + 
            #      "max_rem_mag = {}".format(max_remaining_mag))
            #and remainders is: {}\n".format(remainders))
                
            for cur_rem in remainders:
                cand = pow(10,n-1)*first_digit + cur_rem
                cur_sum = sum_pow_dict(cand,p,p_powers)
                if cur_sum == cand:
                    satisfying_nums.append(cur_sum)
                    #print("p = {}, n = {}, first_digit = {}, cur_rem = {}, cand = {}".format(p, n, first_digit, cur_rem, cand))
            
        else: #no need to check with original limit (max_digit_mag) 
                # -- if no limit here then this limit was also >= 9
                # so check all numbers
            for cur_rem in range(pow(10, n-2), pow(10, n-1) - 1):
                cand = pow(10,n-1)*first_digit + cur_rem
                cur_sum = sum_pow_dict(cand,p,p_powers)
                if cur_sum == cand:
                    satisfying_nums.append(cur_sum)

   
    return satisfying_nums


def solution_5(p): 
    '''  
    TODO: Add Description...
    '''
    p_powers = [pow(k,p) for k in range(10)]
    #print("leading terms:", leading_terms)
    max_digits = get_highest_num_digits(p) #e.g. max_digits = 5 when p = 4
    satisfying_numbers = []
    for num_digits in range(2, max_digits + 1):
        #find all x s.t. n(x) = num_digits and x = sum_four(x)
        cur_values = get_satisfying_n_digit_numbers_5(num_digits, p, p_powers)
        satisfying_numbers.extend(cur_values)
        #print("For {}-digit numbers, found {}\n".format(num_digits, cur_values))
      
    print(satisfying_numbers)
    res = sum(satisfying_numbers)
    
    return res
 

def get_satisfying_n_digit_numbers_6(n, p, p_powers):
    '''
    Explanation...
    '''
    satisfying_nums = [] 
    #max_digit_mag = min(math.ceil(math.pow(math.pow(10,n), 1/p)) - 1,9) 
    max_value = min(pow(10,n) - 1, n*pow(9,p))
    
    for cand in range(pow(10, (n-1)), max_value + 1):
        cur_sum = sum_pow_dict(cand,p,p_powers)
        if cur_sum == cand:
            satisfying_nums.append(cur_sum)
            #print("n = {}, p = {}".format(n, p))

   
    return satisfying_nums


def solution_6(p): 
    '''  
    TODO: Add Description...
    '''
    p_powers = [pow(k,p) for k in range(10)]
    #print("leading terms:", leading_terms)
    max_digits = get_highest_num_digits(p) #e.g. max_digits = 5 when p = 4
    satisfying_numbers = []
    
    for num_digits in range(2, max_digits + 1):
        #find all x s.t. n(x) = num_digits and x = sum_four(x)
        cur_values = get_satisfying_n_digit_numbers_6(num_digits, p, p_powers)
        satisfying_numbers.extend(cur_values)
        #print("For {}-digit numbers, found {}\n".format(num_digits, cur_values))
      
    print(satisfying_numbers)
    res = sum(satisfying_numbers)
    
    return res
 
     

if __name__ == '__main__':
    
    p = 5
    
    start = time.time()
    res_1 = solution_1(p)
    end = time.time()
    print("res_1 = {}\nTook {} seconds".format(res_1, end-start))    
        
    #===========================================================================
    # start = time.time()
    # res_2 = solution_2(p)
    # end = time.time()
    # print("res_2 = {}\nTook {} seconds".format(res_2, end-start))    
    #===========================================================================
     
    start = time.time()
    res_3 = solution_3(p)
    end = time.time()
    print("res_3 = {}\nTook {} seconds".format(res_3, end-start))    
    
    #===========================================================================
    # start = time.time()
    # res_4 = solution_4(p)
    # end = time.time()
    # print("res_4 = {}\nTook {} seconds".format(res_4, end-start))    
    #===========================================================================
     
   
    start = time.time()
    res_5 = solution_5(p)
    end = time.time()
    print("res_5 = {}\nTook {} seconds".format(res_5, end-start))  
 
    start = time.time()
    res_6 = solution_6(p)
    end = time.time()
    print("res_6 = {}\nTook {} seconds".format(res_6, end-start))          
    
    #Answer: 443839 
    
    
       
    
    
    '''
    
    #testing supplementary methods:
    
    For Solution 1:
        
    r = get_highest_num_digits(995)
    #print(r)

    for x in [1634, 8208, 9474]:
        r = sum_pow(x,4)
        #print(r)
        assert(r == x)
        
    #print(2*pow(10,2) + 3*pow(10,3) + 4*pow(10,4) + 5*pow(10,5))
    
    ns = get_satisfying_n_digit_numbers_brute(4, 4)
    print(ns)

    #'''
 

    # For Solution 2
    
    #print(get_nums_with_max_digit_mag(2, 2))
    #print(get_nums_with_max_digit_mag(3, 2))
    #print(get_nums_with_max_digit_mag(2, 4))    
    
    #print(get_n_digit_nums_with_max_digit_mag(3, 2))

    # print(get_highest_num_digits(5))
    # print(log_p(100,5))
    # print(get_satisfying_n_digit_numbers_mag(2,5))
    # print(get_satisfying_n_digit_numbers_mag(3,5))  
    # print(get_satisfying_n_digit_numbers_mag(2,3))
    # print(get_satisfying_n_digit_numbers_mag(3,6))      
    #===========================================================================
    
    # For Solution 3:
    #===========================================================================
    # p = 3
    # p_powers = [pow(k,p) for k in range(10)]
    # print(sum_pow_dict(1295, p, p_powers))
    #===========================================================================


    # For Solution 4:
    #===========================================================================
    #p4 = [pow(k,4) for k in range(10)]
    # p5 = [pow(k,5) for k in range(10)]
    # print(p5)
    #for n = 3, p = 4
    #print([math.floor((p4[k] + 1)/pow(10,2)) for k in range(10)])
    #print(math.ceil(pow(600, 1/4)))
    #print(get_nums_with_max_digit_mag(2, 3))
    #leading_terms = [math.floor((p_powers[k] + 1)/pow(10,n-1)) for k in range(10)]
    #===========================================================================
   
    # For Solution 5:
    
    #print(6*pow(9,5)) 
    #print(math.floor(6*pow(9,5)/pow(10,6-1)))
    
    #print([pow(k,4) for k in range(10)])