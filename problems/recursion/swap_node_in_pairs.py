class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = swap_pairs(new_start)
        return head


if __name__ == '__main__':
    head = ListNode(7)
    one = ListNode(6)
    two = ListNode(5)
    three = ListNode(4)
    four = ListNode(3)
    five = ListNode(2)
    six = ListNode(1)

    head.next = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    result = swap_pairs(head)
    print(f'what is result {result}')

    while result.next:
        result = result.next
        print(f'result: {result.val}')
