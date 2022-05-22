import unittest
# from task_4_head_last import Stack
from task_4_head_first import Stack


class MyTests(unittest.TestCase):
    # tests for task_4_head_last
    # def test_head_last_empty_size(self):
    #     stack = Stack()
    #     self.assertEqual(stack.size(), 0)
    #
    # def test_head_last_empty_pop(self):
    #     stack = Stack()
    #     self.assertEqual(stack.pop(), None)
    #
    # def test_head_last_empty_peek(self):
    #     stack = Stack()
    #     self.assertEqual(stack.peek(), None)
    #
    # def test_head_last_empty_push(self):
    #     stack = Stack()
    #     stack.push(2)
    #     self.assertEqual(stack.size(), 1)
    #     self.assertEqual(stack.peek(), 2)
    #     self.assertEqual(stack.pop(), 2)
    #
    # def test_head_last_5_unit_stack(self):
    #     stack = Stack()
    #     stack.push(1)
    #     self.assertEqual(stack.size(), 1)
    #     for i in range(2, 6):
    #         stack.push(i)
    #     self.assertEqual(stack.size(), 5)
    #     self.assertEqual(stack.pop(), 1)
    #     self.assertEqual(stack.peek(), 5)
    #     stack.pop()
    #     self.assertEqual(stack.size(), 3)

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
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), 5)
        stack.pop()
        self.assertEqual(stack.size(), 3)


if __name__ == '__main__':
    unittest.main()
