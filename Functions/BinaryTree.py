"""A binary tree is a type of tree in which each node has at most two children,
which are referred to as the left child and the right child."""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


"""
A Binary Search Tree is a binary tree with the following properties:
1).The left subtree of a node contains only nodes with values less than the node's value.
2).The right subtree of a node contains only nodes with values greater than the node's value.
3).The left and right subtrees are also binary search trees.
"""


class BinarySearchTree:
    """
    This code defines a basic Binary Search Tree (BST) class with the following methods:

    insert(value): Inserts a value into the BST.
    _insert(node, value): Recursive helper function for insertion.
    in_order_traversal(): Performs an in-order traversal and returns the values.
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return BinaryTreeNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)
