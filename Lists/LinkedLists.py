"""
*********** LINKED LISTS ***************
-> Linked List is a linear Data structure.
-> Contains a Node with two elements; * Data, * Pointer/Reference
"""


# DOUBLY LINKED LIST
class DoubleListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# SINGLY LINKED LISTS
class ListNode:
    def __init__(self, data):
        self.data = data  # Holds the Data
        self.next = None  # Points to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting node at the head
    def insert_at_head(self, data):
        new_node = ListNode(data)    # Create a new Node
        new_node.next = self.head    # Point new node to the current head
        self.head = new_node         # Update head to the new node

    # Inserting at the middle
    def insert_after_node(self,prev_node, data):
        if not prev_node:
            print("The given previous node MUST be in the Linked List.")
            return
        new_node = ListNode(data)    # Create a new Node
        new_node.next = prev_node.next    # Point new node's next to the prev_node's next
        self.head = new_node         # Update prev_node next's to the new node

    # Inserting a new node at the tail/End
    def insert_at_tail(self, data):
        new_node = ListNode(data)    # Create a new Node
        if not self.head:            # If the  List is empty, the new node becomes the head
            self.head = new_node
            return

        current = self.head
        while current.next:          # Traverse to the last node
            current = current.next
        current.next = new_node       # Set the las node's next, to the new node

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete_node(self, key):
        current = self.head
        previous = None

        # Case: Node to be deleted is the Head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Find the Key
        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:  # If node not found
            return

        # Unlink the node from the List
        previous.next = current.next
        current = None



if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_head(0)
    l1.insert_after_node(0,1)
