class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Stack():
    def __init__(self):
        self.store = []

    def push(self, val):
        self.store.append(val)

    def pop(self):
        return self.store.pop()

    def peek(self):
        last_index = len(self.store) - 1
        return self.store[last_index]


def reverse_list(head: ListNode) -> ListNode:
    current_node = head
    stack = Stack()

    while current_node is not None:
        stack.push(current_node.val)
        current_node = current_node.next

    current_node = head

    while current_node is not None:
        val = stack.pop()
        current_node.val = val
        current_node = current_node.next

    return head


def reverse_list_iterative(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    return prev


def reverse_list_recursive(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    pointer = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return pointer


def other_recursive(head: ListNode, prev=None) -> ListNode:
    if not head:
        return prev
    node = head.next
    head.next = prev
    return other_recursive(node, head)


if __name__ == '__main__':
    node_1 = ListNode(4)
    node_2 = ListNode(5)
    node_3 = ListNode(1)
    node_4 = ListNode(9)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    head = reverse_list_recursive(node_1)

    while head is not None:
        print(f'head: {head}')
        head = head.next
