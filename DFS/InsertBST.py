"""
Time complexity -> O(h) where h = height of the tree
Space complexity -> O(h) where h = stack memory
worst case -> o(n) where tree is not balanced
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def insert_bst(bst: Node, val: int) -> Node:
    if bst is None:
        return Node(val)
    if bst.val < val:
        bst.right = insert_bst(bst.right, val)
    elif bst.val > val:
        bst.left = insert_bst(bst.left, val)
    return bst


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)


if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    val = int(input())
    res = insert_bst(bst, val)
    print(' '.join(format_tree(res)))
