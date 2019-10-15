from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_values(l1: ListNode) -> List[int]:
    l1_vals = []
    while l1.next is not None:
        l1_vals.append(l1.val)
        l1 = l1.next
    if l1.val:
        l1_vals.append(l1.val)
    return l1_vals


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_vals = get_values(l1)
    l2_vals = get_values(l2)

    print(f'l1_vals {l1_vals}')
    print(f'l2_vals {l2_vals}')


if __name__ == '__main__':
    l1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)

    l1.next = l1_2
    l1_2.next = l1_3

    l2 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)

    l2.next = l2_2
    l2_2.next = l2_3

    result = add_two_numbers(l1, l2)
    print(f'result -> {result}')
