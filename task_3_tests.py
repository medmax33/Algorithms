from task_3 import DynArray
import unittest


class MyTests(unittest.TestCase):

    # insert without resizing capacity
    def test_insert_without_resizing(self):
        da = DynArray()
        for i in range(15):
            da.append(i)
        da.insert(15, 'a')
        self.assertEqual(da.capacity, 16)
        self.assertEqual(len(da), 16)

    # insert with resizing capacity
    def test_insert_with_resizing(self):
        da = DynArray()
        for i in range(16):
            da.append(i)
        da.insert(15, 'a')
        self.assertEqual(da.capacity, 32)
        self.assertEqual(len(da), 17)

    # insert in a wrong position
    def test_insert_in_wrong_position_minus(self):
        da = DynArray()
        for i in range(64):
            da.append(i)
        with self.assertRaises(IndexError):
            da.insert(-1, 'a')

    def test_insert_in_wrong_position_over_count(self):
        da = DynArray()
        for i in range(64):
            da.append(i)
        with self.assertRaises(IndexError):
            da.insert(87, 'a')

    # delete without resizing capacity
    def test_delete_without_resizing(self):
        da = DynArray()
        for i in range(15):
            da.append(i)
        da.delete(0)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(len(da), 14)

    # delete with resizing capacity to 1.5
    def test_delete_with_resizing(self):
        da = DynArray()
        n = 62
        for i in range(n):
            da.append(i)
        for _ in range(32):
            da.delete(1)
        self.assertEqual(da.capacity, 42)
        self.assertEqual(len(da), 30)

    # delete in a wrong position
    def test_delete_in_wrong_position_minus(self):
        da = DynArray()
        for i in range(32):
            da.append(i)
        with self.assertRaises(IndexError):
            da.insert(-1, 'a')

    def test_delete_in_wrong_position_over_count(self):
        da = DynArray()
        for i in range(33):
            da.append(i)
        with self.assertRaises(IndexError):
            da.insert(34, 'a')


if __name__ == '__main__':
    unittest.main()
