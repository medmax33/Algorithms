import unittest
from task_210 import *


class MyTests(unittest.TestCase):

    def test_me(self):
        s_list = LinkedList2()
        s_list.print_all_nodes()
        s_list.add_in_tail(Node(5))
        s_list.print_all_nodes()
        s_list.add_in_tail(Node(10))
        s_list.print_all_nodes()
        # self.assertEqual(s_list.len(), 0)

    def test_delete(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(5))
        s_list.print_all_nodes()
        s_list.delete(5, True)
        s_list.print_all_nodes()

        # self.assertEqual(s_list.len(), 0)

    def test_insert(self):
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
        # s_list.insert(None, Node('!'))
        s_list.print_all_nodes()
        s_list.insert(n5, Node('-'))
        s_list.print_all_nodes()

    def test_find(self):
        s_list = LinkedList2()
        print(s_list.len())
        n1 = Node(11)
        n2 = Node(22)
        n3 = Node(33)
        n4 = Node(44)
        n5 = Node(55)
        n6 = Node(33)

        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        print(s_list.find_all(33))
        print(s_list.len())

    def test_add_in_head(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node('1-1-1'))
        s_list.print_all_nodes()
        n1 = Node(11)
        n2 = Node(22)
        n3 = Node(33)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.print_all_nodes()
        s_list.add_in_head(Node(74747474))
        s_list.print_all_nodes()

    def test_isinstance(self):
        s_list = LinkedList2()
        n1 = Node(11)
        n2 = Node(22)
        n3 = Node(33)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        node = s_list.head
        while node is not None:
            print(isinstance(node, Dummy))
            node = node.next
        s_list.print_all_nodes()


if __name__ == '__main__':
    unittest.main()

