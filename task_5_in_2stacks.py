class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)
        return None

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[0]


class Queue_stack:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        while self.s1.size() > 0:
            self.s2.push(self.s1.pop())

        self.s1.push(item)

        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())
        return None

    def dequeue(self):
        if self.s1.size() != 0:
            return self.s1.pop()
        return None

    def size(self):
        return self.s1.size()
