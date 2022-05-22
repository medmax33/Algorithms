# Linked List for Stack
class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        # self.stack = []
        self.head = None
        self.tail = None

    def size(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index
        # return len(self.stack)

    def pop(self):
        node = self.tail
        if node is None:
            return None
        else:
            self.tail = node.prev
            node.prev.next = None
            return node

    def push(self, value):
        new_node = Node(value)
        if self.head is not None:
            node = self.head
            new_node.prev = None
            new_node.next = node
            node.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        return None

    def peek(self):
        return self.tail
