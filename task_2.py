class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    # def __str__(self):
    #     return f"[{self.value}]->{self.next}"


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

    # def prnt(self):
    #     node = self.head
    #     print(node)

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

    def delete(self, val, all=False):  # changed
        node = self.head

        while node is not None:
            if node.value == val:
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                    return None
                elif node == self.head:
                    self.head = node.next
                    node.next.prev = None
                    node.next = None
                    node = self.head
                elif node == self.tail:
                    self.tail = node.prev
                    node.prev.next = None
                    node.prev = None
                    return None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node_next = node.next
                    node.next = node.prev = None
                    node = node_next
                if all is False:
                    return None
            else:
                node = node.next
        return None

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
                self.head = newNode
                self.tail = newNode
                newNode.prev = None
                newNode.next = None
                return None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode
                return None

        node = self.head
        while node is not None:
            if node == afterNode:
                break
            if node.next is None:
                return None
            else:
                node = node.next

        if node == self.tail:
            node.next = newNode
            newNode.prev = node
            newNode.next = None
            self.tail = newNode
        else:
            node.next.prev = newNode
            newNode.next = node.next
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
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        return None
