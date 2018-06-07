#!/usr/bin/python3
__author__ = "Alan Au"
__date__   = "2018-06-06"

#This is a programming practice problem:
#Given a sequence of integers, decode them into valid strings of letters.

#1 -> a, 2 -> b, ... 26 -> z
#26 -> z, bf; 21 -> u, ba
#123 -> abc, lc, aw
#101 -> ja

#example = 123
#expected output: abc, lc, aw

import sys #for sys.exit()

#helper functions
def my_chr(my_num):
    #input: str / output: str or None
    offset = 96 #ascii offset
    if int(my_num) > 0 and int(my_num) < 27:
        return chr(int(my_num)+offset) #str
    else:
        return None

def my_pair(num_1, num_2): #str, str
    #input: int,int / output: str or None
    if num_1 == 0:
        return None
    else:
        return my_chr(int( str(num_1)+str(num_2) ))

#main function (recursive)
def decode_sequence(my_str):
    #input: str / output: list
    results = []
    i = len(my_str)
    if i == 0: 
        return results #empty/base case

    #case 1, take char and prepend to all existing results
    new_chr = my_chr(my_str[0])
    if new_chr is not None:
        if i > 1:
            if my_str[1] != '0': #ignore the number starts with "0" case
                old_combos = decode_sequence(my_str[1:]) #call recursively if there's more stuff in sequence
                for old_str in old_combos:
                    new_str = new_chr + old_str
                    results.append(new_str)
        else:
            results.append(new_chr) #otherwise seed a new combination
    
    #case 2, take pair of numbers and prepend to all existing results
    if i > 1:
        new_pair = my_pair(my_str[0],my_str[1])
        if new_pair is not None:
            if i > 2: 
                if my_str[2] != '0': #ignore the number starts with "0" case
                    old_combos = decode_sequence(my_str[2:]) #call recursively if there's more stuff in sequence
                    for old_str in old_combos:
                        new_str = new_pair + old_str
                        results.append(new_str)
            else: 
                results.append(new_pair) #otherwise seed a new combination
    return results

#standalone execution
if __name__ == "__main__":
    #get input here, do some format checking
    example = input("Please enter a sequence of positive integers: ").strip()
    try:
        test = int(example)
        if example[0] == '-':
            sys.exit("Sorry, positive integers only.")
    except ValueError:
        sys.exit("Sorry, badly formed input.")
    #run it here
    print(",".join(decode_sequence(example)))
