#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-18'

import random

#Just for practice, I'm going to implement merge sort.
def mergesort(inlist):
    lenlist = len(inlist)
    half = lenlist//2 #int division
    outlist = []
    if lenlist < 2:
        outlist = inlist #base case for length 1, also handles length 0
    else:
        leftlist = mergesort(inlist[:half])
        rightlist = mergesort(inlist[half:])
        outlist = merge(leftlist, rightlist)
    return outlist
    
def merge(leftlist, rightlist):
    outlist = []
    left = right = 0
    while (left < len(leftlist)) and (right < len(rightlist)):
        if leftlist[left] < rightlist[right]:
            outlist.append(leftlist[left])
            left += 1
        else:
            outlist.append(rightlist[right])
            right += 1
    outlist.extend(leftlist[left:]) #remainder if rightlist is done
    outlist.extend(rightlist[right:]) #remainder if leftlist is done
    return outlist

if __name__ == "__main__":
    my_input = list(range(20))
    random.shuffle(my_input)
    print("input is: ", my_input)
    print("output is:", mergesort(my_input))