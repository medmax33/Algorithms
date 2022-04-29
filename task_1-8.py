from task_1 import Node, LinkedList


def sum_if_equal_length(LinkedList_1, LinkedList_2):
    if LinkedList_1.len() == LinkedList_2.len():
        sum_array = []
        n = LinkedList_1.len()
        a = LinkedList_1.head
        b = LinkedList_2.head
        for _ in range(n):
            sum_array.append(a + b)
            a = a.next
            b = b.next
        return sum_array
    else:
        return None
