import unittest
from task_9 import NativeDictionary


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

nd = NativeDictionary(13)
keys = 'ljdlakjdalk'
values = '01234567890'
# for i in range(1, len(keys)):
#     # print(i, ':', ha.hash_fun(star[:i]), ha.seek_slot(star[:i]))
#     # if ha.seek_slot(star[:i]) is None:
#     #     break
#     ha.put(keys[:i], values[:i])
#
# for i in range(1, len(keys)):
#     print(i, ':', keys[:i], ':', ha.get(keys[:i]))
nd.put('123', 123)
nd.put('123', 555)
print(nd)
print(nd.is_key('123'))
print(nd.is_key('12'))

print(nd.get('123'))
print(nd.get('12'))
