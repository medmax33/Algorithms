import unittest
# import random
from task_5 import Queue


class MyTests(unittest.TestCase):

    def test_insert(self):
        queue = Queue()
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.size(), 5)
        for i in range(5):
            self.assertEqual(queue.dequeue(), i)


if __name__ == '__main__':
    unittest.main()
