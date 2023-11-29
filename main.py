from Functions.Lists import *
from Functions.MyStack import *
from Functions.MyQueue import *
from Functions.LinearSearch import *
from Functions.BinarySearch import *
from Functions.BinaryTree import *
from Functions.Graph import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # ----------- LISTS ---------------#
    my_List = [1, 2, 3, 4, 5]
    reverse_List(my_List)
    print(" ")

    # ----------- STACKS -------------#
    # Create a stack
    my_stack = MyStack()

    # Test the push
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    # Test the pop operation
    print("Popped: ", my_stack.pop())
    print("Is empty? ", my_stack.is_empty())
    print(" ")

    # ---------- QUEUES ----------------#
    # Create my_queue
    my_queue = MyQueue()

    # Test enqueue operation
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    # Test dequeue operation
    print("Dequeued: ", my_queue.dequeue())

    # Check if the Queue is empty
    print("Is empty? ", my_queue.is_empty())
    print(" ")

    # ----------- SEARCH ALGORITHMS -----------#
    # Linear Search - Returns the index  of the target element
    search = SearchAlgo()
    my_searchList = [5, 4, 6, 2, 1, 3, 8, 7]
    target_value = 4
    result = search.linear_search(target_value, my_searchList)
    print(f'Linear Search - Index of {target_value}: {result}')

    # Binary Search
    bSearch = Binary_search()
    # my_sortedList = [1,2,3,4,5,6,7,8,9,10]
    my_sortedList = sorted(my_searchList)
    target_value = 6
    result = bSearch.binary_search(target_value, my_sortedList)
    print(f"Binary Search - Index of {target_value}: {result}")

    # ------------ TREES -----------------------#
    # Binary Tree
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    # Binary Search Tree (BST)
    # Create a Binary Search Tree
    bst = BinarySearchTree()
    values_to_insert = [5, 3, 9, 7, 2, 4, 1, 6, 8, 10]

    for value in values_to_insert:
        bst.insert(value)

    # Perform in-order traversal
    in_order_result = bst.in_order_traversal()
    print("In-Order Traversal:", in_order_result)

    # ------------------ GRAPHS ---------------------#
    # Create a graph
    graph = Graph()

    # Add vertices
    vertices_to_add = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices_to_add:
        graph.add_vertex(vertex)

    # Add edges
    edges_to_add = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])

    # Print the graph
    print("Graph:")
    graph.print_graph()
