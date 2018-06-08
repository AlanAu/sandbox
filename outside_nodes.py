#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2018-06-08'

#This is a short program that, given a binary tree, prints the values of all outside nodes.
#Node values should be output in counter-clockwise order, without duplicates.

#Specifically, this prints all of the leftmost nodes, all of the leaf nodes, and all of the rightmost nodes.
#If a node does not meet one of these conditions, i.e. it's an internal node, it should be skipped.

#Example 1:
#         1
#       /   \
#     2       3
#    / \     / \
#   4   5   6   7
#should print: 1 2 4 5 6 7 3

#Example 2:
#           1
#        /      \
#      2          3
#    /   \      /   \
#   4    5     6     7
#  / \  / \   / \   / \
# 8  9 10 11 12 13 14 15
#should print: 1 2 4 8 9 10 11 12 13 14 15 7 3

class node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_example_1():
    head = node(1,
                node(2,node(4),node(5)),
                node(3,node(6),node(7))
                )
    return head

def build_example_2():
    head = node(1,
                node(2,
                     node(4,node(8),node(9)),
                     node(5,node(10),node(11))
                     ),
                node(3,
                     node(6,node(12),node(13)),
                     node(7,node(14),node(15))
                     )
                )
    return head
    
def outer_left(head, output, seen):
    if head:
        if head.value not in seen:
            seen[head.value] = True
            output.append(head.value)
        if head.left:
            output,seen = outer_left(head.left,output,seen)
    return(output,seen)

def outer_bottom(head, output, seen):
    if head:
        if head.left:
            output,seen = outer_bottom(head.left,output,seen)
        if head.right:
            output,seen = outer_bottom(head.right,output,seen)
        if not head.left and not head.right:
            if head.value not in seen:
                seen[head.value] = True
                output.append(head.value)
    return(output,seen)

def outer_right(head, output, seen):
    if head:
        if head.right:
            output,seen = outer_right(head.right,output,seen)
        if head.value not in seen:
            seen[head.value] = True
            output.append(head.value)
    return(output,seen)

def outside_nodes(head):
    seen = {}
    output = []
    output,seen = outer_left(head,output,seen)
    output,seen = outer_bottom(head,output,seen)
    output,seen = outer_right(head,output,seen)
    return(output)

if __name__ == "__main__":
    head = build_example_2()
    output = list(map(str,outside_nodes(head)))
    print("Output: "+" ".join(output))