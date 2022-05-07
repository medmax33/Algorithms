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
