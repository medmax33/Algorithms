class Node:
    def __init__(self, v=None):
        self.value = v
        self.prev = None
        self.next = None


class Dummy(Node):
    def __init__(self, v=None):
        super().__init__(v)

    # def __bool__(self):
    #     return False


class LinkedList2:
    def __init__(self):
        self.head = Dummy('head')
        self.tail = Dummy('tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        before = self.tail.prev
        item.prev = before
        item.next = self.tail
        before.next = item
        self.tail.prev = item

    def print_all_nodes(self):
        node = self.head.next
        while node is not None:
            if isinstance(node, Dummy) is not True:
                print(node.value)
            node = node.next
        print()

    def delete(self, val, all=False):
        node = self.head.next
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if all is False:
                    return None
            node = node.next
        return None

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head.next == self.tail:
            self.head.next = newNode
            self.tail.prev = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            return None

        if afterNode is None:
            before = self.tail.prev
            before.next = newNode
            self.tail.prev = newNode
            newNode.prev = before
            newNode.next = self.tail
            return None

        node = self.head.next
        while node is not None:
            if node == afterNode:
                break
            if node.next is None:
                return None
            node = node.next

        after = node.next
        node.next = newNode
        after.prev = newNode
        newNode.prev = node
        newNode.next = after
        return None

    def find(self, val):
        node = self.head.next
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head.next
        find_all_array = []
        while node is not None:
            if node.value == val:
                find_all_array.append(node)
            node = node.next
        return find_all_array

    def len(self):
        index = 0
        node = self.head.next
        while node is not None:
            if isinstance(node, Dummy) is not True:
                index += 1
            node = node.next
        return index

    def add_in_head(self, newNode):
        first = self.head.next
        self.head.next = newNode
        first.prev = newNode
        newNode.prev = self.head
        newNode.next = first
        return None
