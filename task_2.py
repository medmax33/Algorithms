class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __str__(self):
        return f"[{self.value}]->{self.next}"


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def prnt(self):
        node = self.head
        print(node)

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

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

        while node is not None:

            if node.value == val:
                if node == self.head and node == self.tail:
                    node.prev = node.next = None
                    self.head = None
                    self.tail = None
                    return None
                elif node == self.head:
                    node_next = node.next
                    self.head = node_next
                    node.prev = node.next = None
                    node_next.prev = self.head
                elif node == self.tail:
                    node_prev = node.prev
                    self.tail = node_prev
                    node_prev.next = None
                    node.prev = node.next = None
                    return None
                else:
                    node_prev = node.prev
                    node_next = node.next
                    node_prev.next = node_next
                    node_next.prev = node_prev
                    node.prev = node.next = None
                if all is False:
                    break
                node = node_next
            else:
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
        if afterNode is None:
            if self.head is None:
                self.head = self.tail = newNode
                newNode.prev = newNode.next = None
                return None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode
                return None

        node = self.head
        while node != afterNode:
            if node.next is not None:
                node = node.next
            else:
                return None

        if node == self.tail:
            self.tail = newNode
            newNode.next = None
            node.next = newNode
            newNode.prev = node
        else:
            newNode.next = node.next
            node.next.prev = newNode
            node.next = newNode
            newNode.prev = node
        return None

    def add_in_head(self, newNode):
        if self.head is not None:
            node = self.head
            newNode.prev = None
            newNode.next = node
            node.prev = newNode
            self.head = newNode
        else:
            self.insert(None, newNode)
        return None
