#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2019-04-08'

# Chess knight valid-moves solver

from collections import deque;

x_max = 8;
y_max = 8;

class coord:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

def visit(board, xy):  # returns dict
    if xy.x not in board:
        board[xy.x] = {};
    board[xy.x][xy.y] = True  # whether seen before or not, it's now True
    return board
    
def is_visited (board, xy):  # returns bool
    if xy.x not in board:
        board[xy.x] = {};
    if xy.y not in board[xy.x]:
        board[xy.x][xy.y] = False  # not seen yet, so must be False
    return board[xy.x][xy.y]
    
def get_moves(board, xy):  # returns list of coord objects
    maybe = [coord(xy.x+1,xy.y+2)]
    maybe.append(coord(xy.x+2,xy.y+1))
    maybe.append(coord(xy.x+2,xy.y-1))
    maybe.append(coord(xy.x+1,xy.y-2))
    maybe.append(coord(xy.x-1,xy.y-2))
    maybe.append(coord(xy.x-2,xy.y-1))
    maybe.append(coord(xy.x-2,xy.y+1))
    maybe.append(coord(xy.x-1,xy.y+2))
    
    moves = []
    for move in maybe:
        if inbounds(move) and not is_visited(board, move):
            moves.append(move)
    return moves

def inbounds(xy):  # returns bool
    if xy.x > 0 and xy.x < x_max:
        if xy.y > 0 and xy.y < y_max:
            return True
    return False

def board_to_list(board):  # returns list of strings
    board_list = []
    for x in board:
        for y in board[x]:
            board_list.append("[{0},{1}]".format(x,y))
    return board_list

if __name__ == "__main__":
    print("Chess knight valid-moves solver")
    max_str = "'"+str(x_max-1)+","+str(y_max-1)+"'"

    try:
        start_x, start_y = list(map(int,input("Please enter a starting location between '0,0' and "+max_str+": ").strip().split(",")))
    except ValueError:
        print("Sorry, unable to parse your input; please enter integer values in the format 'x,y'")
        exit(0)

    if start_x < 0 or start_x >= x_max or start_y < 0 or start_y >= y_max:
        print("Sorry, the starting location must be between '0,0' and "+max_str)
        exit(0)

    start = coord(start_x, start_y)
    to_visit = deque()
    to_visit.append(start)
    board = {}

    while len(to_visit) > 0:
        current = to_visit.popleft()
        board = visit(board, current)
        new_moves = get_moves(board, current)
        to_visit.extend(new_moves)

    print("Reachable locations: "+",".join(board_to_list(board)))