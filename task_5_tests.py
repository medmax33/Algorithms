import unittest
# import random
from task_5 import Queue, rotation
from task_5_in_2stacks import Stack, Queue_stack


class MyTests(unittest.TestCase):

    def test_insert(self):
        queue = Queue()
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.size(), 5)
        for i in range(5):
            self.assertEqual(queue.dequeue(), i)

    def test_rotation(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(queue.size(), 10)
        queue = rotation(queue, 2)
        for i in range(10):
        # self.assertEqual(queue.dequeue(), 5)
            print(queue.dequeue())

        # for i in range(5):
        #     self.assertEqual(queue.dequeue(), i)

    def test_insert_to_stack(self):
        queue = Queue_stack()
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.size(), 5)
        for i in range(5):
            # self.assertEqual(queue.dequeue(), i)
            print(queue.dequeue())


if __name__ == '__main__':
    unittest.main()
