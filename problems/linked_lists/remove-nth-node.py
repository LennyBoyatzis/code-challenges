class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """Removes nth node from end of linked list"""
    node = head
    queue = []

    while node.next:
        if len(queue) < n:
            queue.append(node)
        elif len(queue) == n:
            queue.pop(0)
            queue.append(node)
        node = node.next

    if len(queue) > 1:
        nth_last_node = queue.pop()
        nth_last_node.val = nth_last_node.next.val
        nth_last_node.next = nth_last_node.next.next
    elif len(queue) == 1:
        return []

    return head


if __name__ == '__main__':
    node_1 = ListNode(1)
    head = remove_nth_from_end(node_1, 1)
    print(f'head f{head}')
