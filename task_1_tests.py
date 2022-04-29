import unittest
import random
from task_1 import Node, LinkedList
from


class MyTests(unittest.TestCase):

    # seria of empty tests
    def test_empty_delete(self):
        s_list = LinkedList()
        s_list.delete(0, True)
        self.assertEqual(s_list.len(), 0)

    def test_empty_clean(self):
        s_list = LinkedList()
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_empty_find_all(self):
        s_list = LinkedList()
        self.assertEqual(s_list.find_all(0), [])

    def test_empty_len(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)

    def test_empty_insert_head(self):
        s_list = LinkedList()
        s_list.insert(None, 5)
        self.assertEqual(s_list.len(), 1)

    def test_empty_insert_body(self):
        s_list = LinkedList()
        s_list.insert(0, 5)
        self.assertEqual(s_list.len(), 0)

    # seria of one element tests
    def test_one_delete(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        s_list.delete(0, True)
        s_list.delete(13)
        self.assertEqual(s_list.len(), 0)

    def test_one_clean(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_one_find_all(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        self.assertEqual(s_list.find_all(13), [13])

    def test_one_len(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        self.assertEqual(s_list.len(), 1)

    def test_one_insert_head(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        s_list.insert(None, 5)
        self.assertEqual(s_list.len(), 2)

    def test_one_insert_body(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        s_list.insert(13, 5)
        self.assertEqual(s_list.len(), 2)

    # seria of 100 element tests
    def test_100_delete(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        s_list.delete(1, True)
        self.assertTrue(s_list.len() < 100)

    def test_100_clean(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

    def test_100_find_all(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        self.assertIsNotNone(s_list.find_all(13))

    def test_100_len(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        self.assertEqual(s_list.len(), 100)

    def test_100_insert_head(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        s_list.insert(None, 5)
        self.assertEqual(s_list.len(), 101)

    def test_100_insert_body(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        s_list.insert(13, 5)
        self.assertTrue(s_list.len() > 100)

    def test_summ(self):



if __name__ == '__main__':
    unittest.main()


# n1 = Node(12)
# n2 = Node(55)
# n1.next = n2
# s_list = LinkedList()
# s_list.add_in_tail(n1)
# s_list.add_in_tail(n2)
# s_list.add_in_tail(Node(128))
# s_list.add_in_tail(Node(321))
# s_list.add_in_tail(Node(55))
# s_list.print_all_nodes()

# nf = s_list.find(55)
# if nf is not None:
#     print(nf.value)

# s_list.print_all_nodes()
# print()
#
# # s_list.delete(55, True)
# # s_list.print_all_nodes()
#
# # print(s_list.find_all(321))
# # print(s_list.len())
# s_list.insert(55, 22)
# s_list.print_all_nodes()
