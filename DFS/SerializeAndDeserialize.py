"""
Given a binary tree, write a serialize function that converts the tree into a string and
a deserialize function that converts a string back to a binary tree.

Time complexity -> O(h) where h = height of the tree
Space complexity -> O(h) where h = stack memory
worst case -> o(n) where tree is not balanced
"""
class Node:
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    res = []
    def dfs(root):
        if not root:
            res.append("x")
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ' '.join(res)


def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        if val == 'x':
            return None
        cur = Node(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur
    return dfs(iter(s.split()))

