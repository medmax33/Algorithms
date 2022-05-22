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
        self.stack.append(value)
        return None

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[-1]
