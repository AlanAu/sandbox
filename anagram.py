#Python 3.4
import sys

try:
    word = sys.argv[1]
except:
    print ("usage: anagram.py word")
    exit()

wordhash = {}
for letter in word.lower():
    if letter in wordhash.keys(): wordhash[letter] = wordhash[letter] + 1
    else: wordhash[letter] = 1 #add entry if it isn't already in there

with open("dictionary.txt") as dict: #requires external newline-delimited word list
    printme = True
    for dictword in dict:
        dictword = dictword.rstrip() #get rid of trailing newline
        dicthash = wordhash.copy() #make a fresh copy for each word
        for letter in dictword.lower():
            if letter in dicthash.keys():
                if dicthash[letter] > 1: dicthash[letter] = dicthash[letter] - 1
                else: del dicthash[letter] #remove entry when it would have been decremented to 0
            else: 
                printme = False
                break #can stop checking letters as soon as one of them fails
        if printme: print(dictword) #if passed, print to console
        else: printme = True #if failed, reset flag (without printing)
