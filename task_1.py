class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        node = self.head
        find_all_array = []

        while node is not None:
            if node.value == val:
                find_all_array.append(node)
            node = node.next

        return find_all_array

    def delete(self, val, all=False):
        node = self.head
        node_prev = self.head
        while node is not None:

            if node.value == val:
                if node == self.head:
                    self.head = node.next
                elif node == self.tail:
                    node_prev.next = None
                    self.tail = node_prev
                else:
                    node_prev.next = node.next
                if all is False:
                    break

            node_prev = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def insert(self, afterNode, newNode):
        node = self.head
        new = Node(newNode)
        if afterNode is None:
            self.head = new
            new.next = node
            return None
        else:
            if node is None:
                return None

        node_next = node.next
        while node.value != afterNode:
            node = node.next
            node_next = node.next
        node.next = new
        new.next = node_next
