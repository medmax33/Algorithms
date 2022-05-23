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


def balanced(s: str) -> bool:
    # make empty stack
    skobka = Stack()
    # append each symbol of s in stack
    for letter in s:
        skobka.push(letter)

    # count of open and close round bracket
    pair = 0
    while skobka.size() > 0:
        letter = skobka.pop()
        if letter == '(':
            pair += 1
        elif letter == ')':
            pair -= 1
        else:
            return False
        if pair < 0:
            return False
    if pair % 2 != 0:
        return False
    else:
        return True
