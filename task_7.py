class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
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
        # создаем новый узел
        new = Node(value)

        # если список пустой
        if self.head is None:
            self.head = new
            self.tail = new
            new.prev = None
            new.next = None
            return

        # если список не пустой
        node = self.head
        k = 1 if self.__ascending else -1
        while node is not None:
            # сравнение текущего значения узла с новым узлом
            # с учетом признака упорядоченности

            if self.compare(node.value, value) != k and node.next is None:
                new.prev = node
                new.next = None
                node.next = new
                self.tail = new
                return

            if self.compare(node.value, value) == k and node == self.head:
                new.next = node
                new.prev = None
                node.prev = new
                self.head = new
                return

            if self.compare(node.value, value) != k:
                node = node.next
                continue

            # добавление нового узла
            new.next = node
            new.prev = node.prev
            node.prev.next = new
            node.prev = new
            return

    def find(self, val):
        k = 1 if self.__ascending else -1
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == k:
                return None

            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value != val:
                node = node.next
                continue

            if node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                return
            elif node == self.head:
                self.head = node.next
                node.next.prev = None
                node.next = None
                return
            elif node == self.tail:
                self.tail = node.prev
                node.prev.next = None
                node.prev = None
                return

            node.prev.next = node.next
            node.next.prev = node.prev
            node_next = node.next
            node.next = node.prev = None
            # node = node_next

            return None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def get_all_val(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node.value)
            node = node.next
        return r

    def get_asc(self):
        return self.__ascending

    # testing method
    def print_all_nodes(self):
        node = self.head
        while node is not None:
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
