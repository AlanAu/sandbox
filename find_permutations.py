#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2020-02-24'

'''
Problem: Given an input string, code a function that prints all the permutations of the string.

This problem will return n! results, so for testing purposes, keep it small. 
Also, repeat characters will generate repeat permutations.

This solution is O(n!) because solution set is n! and I have to visit each permutation once.
'''

def find_permutations(my_input):
    my_list = list(my_input)
    output = []
    if len(my_input) == 1:
        return my_list[0]
    for i in range(len(my_list)):
        results = find_permutations(''.join(my_list[:i]+my_list[i+1:]))
        for result in results:
            output.append(my_list[i]+result)
    return(output)

if __name__ == "__main__":
    my_input = "abc"
    print("Input:",my_input,"\nOutput:",find_permutations(my_input))