#! /usr/bin/python3
'''
Programming Practice 
Given a list of numbers and K, return the number of pairs where the sum of the pair is less than K.

Assumes that order of pair does not matter.

Algo notes:
If we work backwards, i.e. the largest values, we get all of the smaller values for free.
Worst case is still O(n!), but average case is O(n*log(n)), incurred by sorting.
'''
__author__ = "Alan Au"
__date__   = "2020-04-20"
__email__  = "alan.au@gmail.com"

def sum_lt_k1(to_sum, k):  # Brute force
    counter = 0
    i = 0
    while i <= len(to_sum)-2:  # Last index - 1 
        j = i+1
        i_val = to_sum[i]
        if i_val >= k:  # Skip if >= k
            continue
        while j <= len(to_sum)-1: # Last index
            j_val = to_sum[j]
            if i_val + j_val < k:
                counter += 1
            j += 1
        i += 1
    return (counter)

def sum_lt_k2 (to_sum, k):  #(list, int) Let's be clever here and try to optimize
    my_sorted = sorted(to_sum, reverse=False)
    counter = 0
    end = len(my_sorted)-1 # Last index
    
    while end >= 1:
        end_val = my_sorted[end]
        if end_val + my_sorted[0] >= k:  # Check for early return, i.e. no pairs here
            end -= 1
            continue
        
        start = end-1
        start_val = my_sorted[start]
        while start >= 0:
            start_val = my_sorted[start]
            if end_val + start_val < k:
                counter += start + 1  # Everything smaller also forms a pair, add 1 b/c 0-index
                break
            else:
                start -= 1
        end -= 1
    return (counter)

if __name__ == "__main__":
    k = 8
    my_input = [1,5,2,4,6,3,9]
    print("Input is: {}\nk is: {}".format(my_input,k))
    print("(1) Number of pairs that sum to less than {}: {}".format(k,sum_lt_k1(my_input,k)))
    print("(2) Number of pairs that sum to less than {}: {}".format(k,sum_lt_k2(my_input,k)))