import unittest
import random
from task_12 import NativeCache


class MyTests(unittest.TestCase):

    def test_true(self):
        cash1 = NativeCache(5)
        print(cash1)

        for _ in range(4):
            cash1.put(str(random.randint(1, 20)), str(random.randint(10000, 20000)))
        print(cash1)

        for _ in range(100):
            cash1.get(str(random.randint(1, 20)))
        print(cash1)

        for _ in range(3):
            s = str(random.randint(100, 200))
            cash1.put(s, 'aaaaa')
            for _ in range(20):
                cash1.get(s)
        print(cash1)

        # self.assertEqual(bloom.is_value(arr[i]), True)
        # self.assertEqual(bloom.is_value(arr[random.randint(0, i)]), True)


# new tetsts
if __name__ == '__main__':
    unittest.main()
