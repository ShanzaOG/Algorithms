class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def Tree_Max_Depth(root: Node) -> int:
    def dfs(root):
        # If root is null return 0; null node adds no depth
        if not root:
            return 0
        # num nodes in the longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) - 1 if root else 0

    # this function builds a tree from input; you don't have to modify it


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = Tree_Max_Depth(root)
    print(res)