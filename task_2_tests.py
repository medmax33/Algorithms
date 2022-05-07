import unittest
import random
from task_2 import Node, LinkedList2


class MyTests(unittest.TestCase):

    # seria of empty tests
    def test_empty_delete(self):
        s_list = LinkedList2()
        s_list.delete(0, True)
        # s_list.prnt()
        self.assertEqual(s_list.len(), 0)

    def test_empty_clean(self):
        s_list = LinkedList2()
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_empty_find_all(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.find_all(0), [])

    def test_empty_find(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.find(0), None)

    def test_empty_len(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.len(), 0)

    def test_empty_insert_head(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(222))
        s_list.insert(None, Node(5))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 2)

    def test_empty_insert_body(self):
        s_list = LinkedList2()
        n1 = Node(0)
        s_list.add_in_tail(n1)
        s_list.insert(n1, Node(5))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 2)

    def test_empty_add_in_head(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node(5))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 1)

    # seria of one element tests
    def test_one_delete(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(13))
        # s_list.prnt()
        # print()
        s_list.delete(13, True)
        # s_list.prnt()
        self.assertEqual(s_list.len(), 0)

    def test_one_clean(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(13))
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_one_find_all(self):
        s_list = LinkedList2()
        n = Node(13)
        s_list.add_in_tail(n)
        self.assertEqual(s_list.find_all(13), [n])

    def test_one_find(self):
        s_list = LinkedList2()
        n = Node(13)
        s_list.add_in_tail(n)
        self.assertEqual(s_list.find(13), n)

    def test_one_len(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(13))
        self.assertEqual(s_list.len(), 1)

    def test_one_insert_head(self):
        s_list = LinkedList2()
        n = Node(13)
        s_list.add_in_tail(n)
        s_list.insert(n, Node(5))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 2)

    def test_one_insert_body(self):
        s_list = LinkedList2()
        n1 = Node(3)
        n2 = Node(5)
        n3 = Node(8)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.insert(n3, Node(13))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 4)

    def test_one_add_in_head(self):
        s_list = LinkedList2()
        n1 = Node(3)
        s_list.add_in_tail(n1)
        s_list.add_in_head(Node(5))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 2)

    # seria of 100 element tests
    def test_20_delete(self):
        s_list = LinkedList2()
        for _ in range(20):
            s_list.add_in_tail(Node(13))  #random.randint(1, 5)))
        # s_list.prnt()
        s_list.delete(13, True)
        # s_list.prnt()
        self.assertTrue(s_list.len() < 20)

    def test_100_clean(self):
        s_list = LinkedList2()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_100_find_all(self):
        s_list = LinkedList2()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        # s_list.prnt()
        print(s_list.find_all(13))
        self.assertIsNotNone(s_list.find_all(13))

    def test_100_find(self):
        s_list = LinkedList2()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        # s_list.prnt()
        print(s_list.find(13))
        self.assertIsNotNone(s_list.find(13))

    def test_100_len(self):
        s_list = LinkedList2()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        self.assertEqual(s_list.len(), 100)

    def test_10_insert_tail(self):
        s_list = LinkedList2()
        # for _ in range(10):
        #     s_list.add_in_tail(Node(random.randint(1, 20)))

        n1 = Node(11)
        n2 = Node(22)
        n3 = Node(33)
        n4 = Node(44)
        n5 = Node(55)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)

        # s_list.prnt()
        s_list.insert(n1, Node(-1))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 6)

    def test_5_insert_body(self):
        s_list = LinkedList2()
        n1 = Node(11)
        n2 = Node(22)
        n3 = Node(33)
        n4 = Node(44)
        n5 = Node(55)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        # s_list.prnt()
        s_list.insert(n5, Node('-'))
        # s_list.prnt()
        self.assertTrue(s_list.len() > 5)

    def test_20_add_in_head(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(111))
        for _ in range(20):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        # s_list.prnt()
        s_list.add_in_head(Node(-1))
        # s_list.prnt()
        self.assertEqual(s_list.len(), 22)

    # delete all test
    def test_delete_all(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(123))
        for _ in range(2):
            s_list.add_in_tail(Node(3))
        for _ in range(3):
            s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(333))
        for _ in range(2):
            s_list.add_in_tail(Node(3))
        s_list.add_in_tail(Node(333))
        # s_list.prnt()
        s_list.delete(7, True)
        # s_list.prnt()
        self.assertTrue(s_list.len() < 11)


if __name__ == '__main__':
    unittest.main()
