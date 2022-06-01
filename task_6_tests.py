import unittest
from task_6 import Deque, palindrom


class MyTests(unittest.TestCase):

    def test_insert(self):
        dequeue = Deque()
        for i in range(10):
            if i % 2 == 0:
                dequeue.addFront(i)
            else:
                dequeue.addTail(i - 10)
        self.assertEqual(dequeue.size(), 10)

    def test_primer(self):
        deq = Deque()
        deq.addFront("f1")
        deq.addTail("t1")
        deq.addFront("f2")
        deq.addTail("t2")
        while deq.size() > 0:
            print(deq.removeFront())
            print(deq.removeTail())

    def test_palindrom(self):
        print(palindrom('А роза упала на лапу Азора'))

    def test_add_remove_Front(self):
        deq = Deque()
        for i in range(1, 1001):
            deq.addFront(i)
            self.assertEqual(deq.size(), i)
            self.assertEqual(deq.into(i), True)
            self.assertEqual(deq.into(i + 1), False)
        for i in range(1, 1001):
            self.assertEqual(deq.into(1001 - i), True)
            deq.removeFront()
            self.assertEqual(deq.into(1001 - i), False)
            self.assertEqual(deq.size(), 1000 - i)

    def test_add_Tail_remove_Front(self):
        deq = Deque()
        for i in range(1, 1001):
            deq.addTail(i)
            self.assertEqual(deq.size(), i)
            self.assertEqual(deq.into(i), True)
            self.assertEqual(deq.into(i + 1), False)
        for i in range(1, 1001):
            self.assertEqual(deq.into(i), True)
            self.assertEqual(deq.removeFront(), i)
            self.assertEqual(deq.into(i), False)
            self.assertEqual(deq.size(), 1000 - i)


if __name__ == '__main__':
    unittest.main()
