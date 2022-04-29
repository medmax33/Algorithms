from task_1 import Node, LinkedList

n1 = Node(12)
n2 = Node(55)
n1.next = n2
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(321))
s_list.add_in_tail(Node(55))
# s_list.print_all_nodes()

# nf = s_list.find(55)
# if nf is not None:
#     print(nf.value)

s_list.print_all_nodes()
print()
s_list.delete(55, True)
s_list.print_all_nodes()
