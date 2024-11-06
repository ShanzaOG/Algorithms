"""
Given a binary tree, return the rightmost node of each level.

It should be noted that at each level there can only be at most one rightmost node.

-> Input : : : >    1 2 4 x 7 x x 5 x x 3 x 6 x x
-> Output : : : >   1 3 6 7
------------------------------------------- SOLUTION DESIGN -----------------------------
# Approach 1
    *First, check if we have any node. If not return []
    *Create a List to hold the final result; res = []
    *Create a list to hold nodes of each level./ But the catch is how do I get the right outermost node
    *If I get the outermost level, append to res = [] and move on to the next level

    ---> Filed because I did not account for the right most val and we don't need nodes in new_level.
    ---> Failed because I did not account for addition of child nodes to queue

# Approach 2
    *First Create a list to hold the result; res = []
    *The make sure at least one node is present; queue = deque([root])
    *Traversing through the tree in level oder, append the outermost node; res.append(queue[0].val)
    *Append the right child first in the queue so that it may be found first during appendage to res = []
    *return res[]
"""
from typing import List, Deque
from collections import deque


class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def binary_tree_right_side_view(root: Node) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    queue = deque([root])  # At least one element should be in the queue
    while len(queue) > 0:
        n = len(queue)
        res.append(queue[0].val)
        for _ in range(n):
            node = queue.popleft()
            for child in [node.right, node.left]:  # Add right child so that it will pop out of the queue first
                if child is not None:
                    queue.append(child)

    return res



def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = binary_tree_right_side_view(root)
    print(" ".join(map(str, res)))
