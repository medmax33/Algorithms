import unittest
from task_8 import HashTable


# class MyTests(unittest.TestCase):
#
#     def test_add_True(self):
#         order = OrderedList(True)
#         order.add(2)
#         order.add(1)
#         order.add(0)
#         order.add(-1)
#         self.assertEqual(order.get_all_val(), [-1, 0, 1, 2])
#
#
# if __name__ == '__main__':
#     unittest.main()

ha = HashTable(128, 5)
print(ha.hash_fun('2;lakjndsakjdnskfakfjdsfsdaofjow'))
