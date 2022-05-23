import unittest
# import random
# from task_4_head_last import Stack
from task_4 import Stack, balanced


class MyTests(unittest.TestCase):

    # tests for task_4_head_first
    def test_head_first_empty_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_head_first_empty_pop(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)

    def test_head_first_empty_peek(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)

    def test_head_first_empty_push(self):
        stack = Stack()
        stack.push(2)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)

    def test_head_first_5_unit_stack(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        for i in range(2, 6):
            stack.push(i)
        self.assertEqual(stack.size(), 5)
        # self.assertEqual(stack.pop(), 5)
        # self.assertEqual(stack.peek(), 4)
        # print(stack.pop())
        # self.assertEqual(stack.size(), 3)
        for i in range(5, 0, -1):
            self.assertEqual(stack.pop(), i)

    def test_from_task(self):
        stack = Stack()
        for i in range(100, 0, -1):
            stack.push(i)
        # stack.push(1)
        # stack.push("2")
        # stack.pop()
        # stack.push(3.14)
        while stack.size() > 0:
            print(stack.size(), '-', stack.pop())

    def test_Balanced(self):
        self.assertEqual(balanced('(()((()())()))'), True)


if __name__ == '__main__':
    unittest.main()
