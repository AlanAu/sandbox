#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2020-02-24'

'''
Problem: Given two sorted integer arrays, find the pair, one element from each array, with the minimum distance. 

Brute force is to just do a full pairwise comparison between both arrays. O(n^2)

Optimized version that takes advantage of sorted: O(n) (but sort costs O(n*log(n))
Advance through each list, whichever has the lower number, until end of lists.
'''

# Brute force method, O(n^2)
def find_nearest_pair_1(a,b):
    # Initialize with first pair
    min_dist = abs(b[0] - a[0])
    nearest = [a[0],b[0]] 
    for i in range(len(a)):
        for j in range(len(b)):
            dist = abs(b[j] - a[i])
            if dist < min_dist:
                min_dist = dist
                nearest = [a[i],b[j]]
    return (nearest)

# Optimized version, O(n))
def find_nearest_pair(a,b):
    # Initialize with first pair
    min_dist = abs(b[0] - a[0])
    nearest = [a[0],b[0]] 
    i = 0; j = 0
    
    while i < len(a) and j < len(b):
        dist = abs(b[j] - a[i])
        if dist < min_dist:
            min_dist = dist
            nearest = [a[i],b[j]]
        if a[i] < b[j] and i < len(a)-1: # If a < b and not at end, go to next 'a' value
            i += 1
        else: # Otherwise: (b <= a) or (a is at end) or (largest b < smallest a)
            j += 1
    return (nearest)

if __name__ == '__main__':
    a = [1,2,4,8,49]
    b = [5,10,25,50]
    print('input 1:',a,'\ninput 2:',b,'\nnearest pair:',find_nearest_pair(a,b))