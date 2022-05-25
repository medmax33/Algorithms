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
    # check if first symbol not (
    if s[0] != '(':
        return False

    # make empty stack
    skobka = Stack()

    # push in stack if symbol is (,
    # pop stack if symbol is )
    for letter in s:
        # if symbol neither ( not ) return False
        if letter != '(' and letter != ')':
            return False

        if letter == '(':
            skobka.push(letter)
            continue

        if letter == ')' and skobka.size() > 0:
            skobka.pop()
            continue

        return False

    if skobka.size() == 0:
        return True

    return False
