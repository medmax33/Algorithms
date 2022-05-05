import unittest
import random
from task_1 import Node, LinkedList
from task_1_8 import sum_if_equal_length


class MyTests(unittest.TestCase):

    # seria of empty tests
    def test_empty_delete(self):
        s_list = LinkedList()
        s_list.delete(0, False)
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
        s_list.insert(None, Node(5))
        self.assertEqual(s_list.len(), 1)

    def test_empty_insert_body(self):
        s_list = LinkedList()
        n1 = Node(0)
        s_list.add_in_tail(n1)
        s_list.insert(n1, Node(5))
        s_list.prnt()
        self.assertEqual(s_list.len(), 2)

    # seria of one element tests
    def test_one_delete(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(13))
        s_list.print_all_nodes()
        print()
        s_list.delete(13, True)
        s_list.print_all_nodes()
        # s_list.delete(13)
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
        s_list.insert(None, Node(5))
        s_list.prnt()
        self.assertEqual(s_list.len(), 2)

    def test_one_insert_body(self):
        s_list = LinkedList()
        n1 = Node(3)
        n2 = Node(5)
        n3 = Node(8)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.insert(n2, Node(13))
        s_list.prnt()
        self.assertEqual(s_list.len(), 4)

    # seria of 100 element tests
    def test_100_delete(self):
        s_list = LinkedList()
        for _ in range(100):
            s_list.add_in_tail(Node(random.randint(1, 20)))
        s_list.delete(1, False)
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
        s_list.insert(None, Node(-1))
        s_list.prnt()
        self.assertEqual(s_list.len(), 101)

    def test_100_insert_body(self):
        s_list = LinkedList()
        n1 = Node('ch')
        # s_list.add_in_tail(n1)
        for _ in range(20):
            k = random.randint(1, 5)
            if k == 5:
                n2 = n1
            else:
                n2 = Node(k)
            s_list.add_in_tail(n2)
        s_list.prnt()
        s_list.insert(n1, Node('-'))
        s_list.prnt()
        self.assertTrue(s_list.len() > 19)

    def test_summ(self):
        a = LinkedList()
        b = LinkedList()
        for _ in range(5):
            a.add_in_tail(Node(_))
            b.add_in_tail(Node(_ + 10))
        self.assertEqual(sum_if_equal_length(a, b), [10, 12, 14, 16, 18])

    # delete all test
    def test_delete_all(self):
        s_list = LinkedList()
        for _ in range(4):
            s_list.add_in_tail(Node(3))
        for _ in range(3):
            s_list.add_in_tail(Node(5))
        s_list.print_all_nodes()
        print()
        s_list.delete(5, False)
        s_list.print_all_nodes()
        self.assertTrue(s_list.len() < 100)

    def test_insert_tail(self):
        s_list = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.prnt()
        s_list.insert(n3, Node('-'))
        s_list.prnt()
        self.assertTrue(s_list.len() == 4)


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
