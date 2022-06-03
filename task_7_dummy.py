class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class Dummy(Node):
    def __init__(self, v=None):
        super().__init__(v)


class OrderedList:
    def __init__(self, asc):
        self.head = Dummy()
        self.tail = Dummy()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.__ascending = asc

    def compare(self, v1, v2):
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
        if v1 is None:
            return 1 if self.__ascending else -1
        elif v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        # автоматическая вставка value в нужную позицию
        node = self.head.next
        while node is not None:
            k = 1 if self.__ascending else -1
            if self.compare(node.value, value) != k:
                node = node.next
                continue

            node_new = Node(value)
            node_new.prev = node.prev
            node_new.next = node
            node.prev.next = node_new
            node.prev = node_new
            return None

    def find(self, val):
        k = 1 if self.__ascending else -1
        node = self.head.next
        while node is not None:
            if self.compare(node.value, val) == k:
                return None

            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head.next
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                return None
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        index = 0
        node = self.head.next
        while node is not None:
            if isinstance(node, Dummy) is not True:
                index += 1
            node = node.next
        return index

    def get_all(self):
        r = []
        node = self.head.next
        while node is not None:
            if isinstance(node, Dummy) is not True:
                r.append(node)
            node = node.next
        return r

    def get_all_val(self):
        r = []
        node = self.head.next
        while node is not None:
            if isinstance(node, Dummy) is not True:
                r.append(node.value)
            node = node.next
        return r

    def get_asc(self):
        return self.__ascending

    # testing method
    def print_all_nodes(self):
        node = self.head.next
        while node is not None:
            if isinstance(node, Dummy) is not True:
                print(node.value)
            node = node.next
        print()


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
        if v1 is None:
            return 1 if self.get_asc() else -1

        # clear extra spaces
        v1_1 = v1.strip()
        v2_1 = v2.strip()

        if v1_1 < v2_1:
            return -1
        elif v1_1 > v2_1:
            return 1
        return 0
