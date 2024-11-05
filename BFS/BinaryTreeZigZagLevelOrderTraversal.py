"""
Given a binary tree, return its level order traversal but in alternating left-to-right order.
Input -> 1 2 4 x 7 x x 5 x 8 x x 3 x 6 x x
Output ->
            1
            3 2
            4 5 6
            8 7
"""

from typing import List, Deque
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root: Node) -> List[List[int]]:
    # Code
    res = []
    queue = deque([root])
    left_to_right = True

    if not root: # Handling edge-case scenario
        return []

    while len(queue) > 0: # At least we have an element in the queue
        n = len(queue)
        new_level: Deque[int] = deque() # Create and initialize new_level to hold int only as a deque

        for _ in range(n):
            node = queue.popleft()
            if left_to_right:
                new_level.append(node.val)
            else:
                new_level.appendleft(node.val)

            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)
        left_to_right = not left_to_right
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
    res = zig_zag_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))
