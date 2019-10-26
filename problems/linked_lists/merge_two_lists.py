class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """Merge 2 sorted linked lists and return as 1"""
    prehead = ListNode(-1)

    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    prev.next = l1 if l1 is not None else l2

    return prehead.next


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(4)
    node_3 = ListNode(5)
    node_4 = ListNode(9)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_10 = ListNode(10)
    node_11 = ListNode(11)
    node_12 = ListNode(12)
    node_13 = ListNode(13)

    node_10.next = node_11
    node_11.next = node_12
    node_12.next = node_13

    head = merge_two_lists(node_1, node_10)

    while head is not None:
        print(f'head: {head.val}')
        head = head.next
