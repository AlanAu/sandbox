#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2020-01-07'

'''
Bowling score calculator (coding practice)

Game is 10 frames. 10 pins are set up, and you have up to 2 throws to knock down pins.
Your total score is the cumulative number of pins you knock down over 10 frames.
If all pins knocked down during first throw, that's a "strike." This ends the frame. Add pins knocked down during next 2 throws.
If all pins knocked down after second throw, that's a "spare." Add pins knocked down during next 1 throw.
After frame 10, you can finish your extra throw/throws, but they are not part of a new frame and cannot accumulate more extra throws.
'''

def get_score(throws): # input: list of ints
    score = 0
    throw = 0
    frame = 0
    while (throw < len(throws)-1) and (frame < 10):
        throw_1 = throws[throw]
        throw_2 = throws[throw + 1]
        if throw < len(throws)-2:
            throw_3 = throws[throw + 2]
        # standard frame, score += 2 throws
        if throw_1 + throw_2 < 10:
            score += throw_1 + throw_2
            throw += 2 # next frame
        # spare, score += (2 throws + 1 throw)
        elif throw_1 + throw_2 == 10:
            score += throw_1 + throw_2 + throw_3
            throw += 2 # next frame
        # strike, score += (1 throw + 2 throws)
        elif throw_1 == 10:
            score += throw_1 + throw_2 + throw_3
            throw += 1 # next frame (strike)
        # advance frame conuter
        frame += 1
    return (score)

if __name__ == "__main__":
    throws = [10,10,10,10,10,10,10,10,10,10,10,10] # test input, output should be 300
    throws = [2,3, 4,1, 10, 3,1, 4,6, 3,2, 10, 2,3, 4,0, 3,1] # test input, output should be 74
    print("Score for",throws,"is:",get_score(throws))