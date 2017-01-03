#Python 3.4
import sys

try:
    word = sys.argv[1]
except:
    print ("usage: anagram.py word")
    exit()

wordhash = {}
for letter in word.lower():
    if letter in wordhash.keys(): wordhash[letter] = int(wordhash[letter]) + 1
    else: wordhash[letter] = 1

with open("dictionary.txt") as dict: #requires external newline-delimited word list
    printme = True
    for dictword in dict:
        dictword = dictword.rstrip() #get rid of trailing newline
        dicthash = wordhash.copy() #make a fresh copy for each word
        for letter in dictword.lower():
            if letter in dicthash.keys():
                if dicthash[letter] > 1: dicthash[letter] = dicthash[letter] - 1
                else: del dicthash[letter]
            else: 
                printme = False
                break
        if printme: print(dictword)
        else: printme = True