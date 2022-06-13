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
star = 'lkjdlakjdlakjdlaladsjfoaicmewi7du73mdlsakjdasikdjlakdjlsaknmclksdjfiweuhfemdpOdkpewdjoewaimkdmjewoijdewaoijdapowkdpqOWKDPOIWQJDOIJEWkjkj'
for i in range(len(star)):
    print(i, ':', ha.hash_fun(star[:i]), ha.seek_slot(star[:i]))
    if ha.seek_slot(star[:i]) is None:
        break
    ha.put(star[:i])
print(ha.find('lkjdlakjdlakjdlaladsjfoaicmewi7du73mdlsakjdasikdjlakdjlsaknmclksdjfiweuhfemdpOdkpewdj'))