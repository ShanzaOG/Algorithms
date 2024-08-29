class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def visible_tree_node(root: Node) -> int:
    def dfs_root(root, max_sofar):
        if not root:
            return 0

        total = 0
        if root.val >= max_sofar:
            total += 1

        total += dfs_root(root.left, max(max_sofar, root.val))
        total += dfs_root(root.right, max(max_sofar, root.val))

        return total

    return dfs_root(root, -float('inf'))


def build_tree_nodes(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
    left = build_tree_nodes(nodes, f)
    right = build_tree_nodes(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree_nodes(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)