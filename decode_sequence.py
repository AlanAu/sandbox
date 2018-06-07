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
        return results #empty case

    #case 1, take char and prepend to all existing results
    new_chr = my_chr(my_str[0])
    if new_chr is not None:
        if i > 1:
            if my_str[1] != '0':
                old_combos = decode_sequence(my_str[1:])
                for old_str in old_combos:
                    new_str = new_chr + old_str
                    results.append(new_str)
        else:
            results.append(new_chr)
    
    #case 2
    if i > 1:
        new_pair = my_pair(my_str[0],my_str[1])
        if new_pair is not None:
            if i > 2:
                if my_str[2] != '0':
                    old_combos = decode_sequence(my_str[2:])
                    for old_str in old_combos:
                        new_str = new_pair + old_str
                        results.append(new_str)
            else:
                results.append(new_pair)
    return results

#standalone execution
if __name__ == "__main__":
    example = input("Please enter a sequence of numbers: ").strip()
    try:
        test = int(example)
        if example[0] == '-':
            sys.exit("Sorry, positive integers only.")
    except ValueError:
        sys.exit("Sorry, badly formed input.")
    print(",".join(decode_sequence(example)))
