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
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        return [] # здесь будет ваш код

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
        return None

    def clean(self):
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код