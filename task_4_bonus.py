from task_4 import Stack


def postfix(s: str) -> int:
    stack1 = Stack()
    stack2 = Stack()

    # refactored queue of appending elements to stack
    # because of my mistake in main task
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            stack1.push(int(s[i]))
        elif s[i] in {'+', '*', '-', '/', '='}:
            stack1.push(s[i])
        # if element not digit, arithmetic operation or space
        # we have an error
        elif s[i] != ' ':
            raise TypeError

    while stack1.size() > 0:
        element = stack1.pop()
        if type(element) == int:
            stack2.push(element)
        elif element == '+':
            stack2.push(stack2.pop() + stack2.pop())
        elif element == '*':
            stack2.push(stack2.pop() * stack2.pop())
        elif element == '-':
            # we pop stack elements in reverse order
            # first Вычитаемое second Уменьшаемое
            stack2.push(-stack2.pop() + stack2.pop())
        elif element == '/':
            # we pop stack elements in reverse order
            # first Делитель second Делимое
            stack2.push((1 / stack2.pop()) * stack2.pop())
        elif element == '=':
            return stack2.pop()

    if stack2.size() == 1:
        return stack2.pop()

    raise RuntimeError('Отсуствует завершающий оператор')
