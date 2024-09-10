"""
Given a binary tree, return its level order traversal. The input is the root node of the tree.
The output should be a list of lists of integers, with the ith list containing the values of nodes on level i,
 from left to right.
"""

from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Node) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    queue = deque([root]) # At least one element is in the queue
    while len(queue) > 0: # As long as there is an element in the queue
        n = len(queue) # Number of nodes in the current level
        new_level = []
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]: # Enqueue non-null children
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
