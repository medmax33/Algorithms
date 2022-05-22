from task_4 import Stack


def postfix(s: str) -> int:
    stack1 = Stack()
    stack2 = Stack()
    for i in s:
        if i == ' ':
            continue
        elif i.isdigit():
            stack1.push(int(i))
        elif i in {'+', '*', '='}:
            stack1.push(i)
        else:
            return 1000000000000

    while stack1.size() > 0:
        element = stack1.pop()
        if type(element) == int:
            stack2.push(element)
        elif element == '+':
            stack2.push(stack2.pop() + stack2.pop())
        elif element == '*':
            stack2.push(stack2.pop() * stack2.pop())
        else:
            return stack2.pop()
