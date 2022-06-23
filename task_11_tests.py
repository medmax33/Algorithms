import unittest
import random
from task_11 import BloomFilter
import time


class MyTests(unittest.TestCase):

    def test_put(self):
        bloom = BloomFilter(32)
        # arr = ['0123456789', '1234567890', '2345678901',
        #        '3456789012', '4567890123', '5678901234',
        #        '6789012345', '7890123456', '8901234567',
        #        '9012345678', 'abcdefgh']

        arr = ['lksjadlak', '.s,ma.,mas', 'lkjdlaksjdl',
               ';lokwokd', 'poipoiwe9', 'xadXR',
               'LKJSQJSP', 'lkjdlks', 'kjsdoqiwjd',
               ';sodkpak', 'abcdefgh']


        # bloom.add(arr[0])
        # bloom.add(arr[1])
        # bloom.add(arr[2])
        for i in range(10):
            print(bloom.hash1(arr[i]), bloom.hash2(arr[i]))
        # print(bloom.is_value(arr[3]))

        for i in range(10):
            bloom.add(arr[i])
            self.assertEqual(bloom.is_value(arr[i]), True)
            self.assertEqual(bloom.is_value(arr[random.randint(0, i)]), True)
            self.assertEqual(bloom.is_value(arr[i+1]), False)


if __name__ == '__main__':
    unittest.main()
