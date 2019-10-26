class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    """Removes node in place from linked list"""
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    node_1 = ListNode(4)
    node_2 = ListNode(5)
    node_3 = ListNode(1)
    node_4 = ListNode(9)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
