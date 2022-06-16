import unittest
import random
from task_10 import PowerSet
import time


class MyTests(unittest.TestCase):

    def test_put(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set1.put('1234')
        self.assertEqual(set1.put('1234'), False)
        self.assertEqual(set1.put('1235'), True)

    def test_remove(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set1.put('1234')
        set1.remove('1234')
        self.assertEqual(set1.get('1234'), False)

    def test_intersection_not_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(4):
            set1.put(str(random.randint(0, 4)))
        for i in range(3):
            set2.put(str(random.randint(0, 4)))
        self.assertGreater(set1.intersection(set2).size(), 0)

    def test_intersection_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(120):
            set1.put(str(random.randint(0, 120)))
        for i in range(70):
            set2.put(str(random.randint(121, 222)))
        self.assertEqual(set1.intersection(set2).size(), 0)

    def test_union(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(1, 22):
            set1.put(str(1 * i))
        self.assertEqual(set1.union(set2).size(), 21)
        for i in range(1, 18):
            set2.put(str(30 * i))
        self.assertEqual(set1.union(set2).size(), 38)

    def test_difference(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(1, 20):
            set1.put(str(i))
        for i in range(1, 10):
            set2.put(str(i))
        self.assertEqual(set1.difference(set2).size(), 10)
        for i in range(10, 20):
            set2.put(str(i))
        self.assertEqual(set1.difference(set2).size(), 0)

    def test_issubset(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(1, 20):
            set1.put(str(i))
        for i in range(1, 10):
            set2.put(str(i))
        self.assertEqual(set1.issubset(set2), True)
        for i in range(10, 22):
            set2.put(str(i))
        self.assertEqual(set1.issubset(set2), False)

    def test_issubset_not_all(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(1, 20):
            set1.put(str(i))
        for i in range(1, 10):
            set2.put(str(random.randint(1, 100)))
        self.assertEqual(set1.issubset(set2), False)

    def test_time(self):
        start = int(time.time())
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(2000):
            set1.put(str(random.randint(1, 20000)))
            set2.put(str(random.randint(1, 20000)))
        print(set1.difference(set2))
        finish = int(time.time())
        self.assertTrue(finish - start < 2)


if __name__ == '__main__':
    unittest.main()
