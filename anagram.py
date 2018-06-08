#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2018-06-08'

#This is practice code to list anagrams and substring-anagrams of a word.

import sys

external_dict = "./dictionary.txt" #newline-delimited word list

try:
    word = sys.argv[1].lower()
except:
    sys.exit("usage: anagram.py word")

word_hash = {}
for letter in word:
    if letter in word_hash: 
        word_hash[letter] = word_hash[letter] + 1
    else: 
        word_hash[letter] = 1

with open(external_dict) as dictionary: 
    print_word = True
    for dict_word in dictionary:
        dict_word = dict_word.rstrip().lower()
        my_word = word_hash.copy() #make fresh copy
        
        for letter in dict_word:
            if letter in my_word:
                if my_word[letter] > 1: 
                    my_word[letter] = my_word[letter] - 1
                else: 
                    del my_word[letter]
            else: 
                print_word = False
                break #if fails, don't need to check the rest
        
        if print_word: 
            print(dict_word)
        print_word = True