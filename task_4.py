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
        if letter == '(' or letter == ')':
            skobka.push(letter)
            continue
        return False

    # check if last symbol not )
    if skobka.peek() != ')':
        return False

    # count of open and close round bracket
    balance = Stack()
    while skobka.size() > 0:
        letter = skobka.pop()
        if letter == ')':
            balance.push(letter)
            continue

        if letter == '(' and balance.size() > 0:
            balance.pop()
            continue

        return False

    if balance.size() == 0:
        return True

    return False
