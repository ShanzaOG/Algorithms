"""
--> Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
To find the Lowest Common Ancestor of two nodes in a BST, we break our search into 3 common cases:

    1. If nodes p and q are on the left of the current node, then continue search the left side
    2. If nodes p and q are on the right of the current node, then continue search the right side
    3. If nodes p and q are split (one is on the left, the other is on the right), then we can return the current node
       as the LCA.

Time complexity -> O(h) where h = height of the tree
Space complexity -> O(h) where h = stack memory
worst case -> o(n) where tree is not balanced
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def lca_on_bst(bst: Node, x: int, y: int):
    """
    :param bst: tree
    :param x: node1
    :param y: node2
    :return: The value of the LCA between nodes x and y
    """
    if x < bst.val and y < bst.val:
        return lca_on_bst(bst.left, x, y)
    elif x > bst.val and y > bst.val:
        return lca_on_bst(bst.left, x, y)
    else:
        return bst.val


