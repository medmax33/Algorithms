import unittest
from task_7 import OrderedList, OrderedStringList


class MyTests(unittest.TestCase):

    def test_add_True(self):
        order = OrderedList(True)
        order.add(2)
        order.add(1)
        order.add(0)
        order.add(-1)
        self.assertEqual(order.get_all_val(), [-1, 0, 1, 2])

    def test_add_False(self):
        order = OrderedList(False)
        order.add(9)
        order.add(3)
        order.add(8)
        order.add(7)
        self.assertEqual(order.get_all_val(), [9, 8, 7, 3])

    def test_delete_True(self):
        order = OrderedList(True)
        order.add(2)
        order.add(3)
        order.add(8)
        order.add(7)
        order.delete(3)
        self.assertEqual(order.get_all_val(), [2, 7, 8])

    def test_delete_False(self):
        order = OrderedList(False)
        order.add(2)
        order.add(3)
        order.add(8)
        order.add(7)
        order.delete(7)
        self.assertEqual(order.get_all_val(), [8, 3, 2])

    def test_delete_None(self):
        order = OrderedList(False)
        order.add(2)
        order.add(3)
        order.add(8)
        order.add(7)
        order.delete(10)
        self.assertEqual(order.get_all_val(), [8, 7, 3, 2])

    def test_find_True(self):
        order = OrderedList(True)
        order.add(2)
        order.add(3)
        order.add(8)
        order.add(7)
        self.assertTrue(order.find(3) is not None)
        self.assertTrue(order.find(4) is None)


    def test_find_False(self):
        order = OrderedList(False)
        order.add(2)
        order.add(3)
        order.add(8)
        order.add(7)
        self.assertTrue(order.find(3) is not None)
        self.assertTrue(order.find(4) is None)

    def test_order_string_True(self):
        str_order = OrderedStringList(True)
        str_order.add('kj j')
        str_order.add('  qkj aj ')
        str_order.add('     b kj j   ')
        str_order.add('     bk j  c ')
        self.assertEqual(str_order.get_all_val(), ['     b kj j   ',
                                                   '     bk j  c ',
                                                   'kj j',
                                                   '  qkj aj '])

    def test_order_string_False(self):
        str_order = OrderedStringList(False)
        str_order.add('kj j')
        str_order.add('  qkj aj ')
        str_order.add('     b kj j   ')
        str_order.add('     bk j  c ')
        self.assertEqual(str_order.get_all_val(), ['  qkj aj ',
                                                   'kj j',
                                                   '     bk j  c ',
                                                   '     b kj j   '])


if __name__ == '__main__':
    unittest.main()
