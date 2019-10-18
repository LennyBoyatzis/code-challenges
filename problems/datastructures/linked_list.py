class Node():
    def __init__(self, value=None, node=None):
        self.value = value
        self.next = next

    def get_data(self):
        pass

    def get_next(self):
        pass

    def set_next(self):
        pass


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert_end(self):
        """Inserts element at end"""
        pass

    def insert_head(self):
        """Inserts element at start"""
        pass

    def delete(self):
        """Delete given element"""
        pass

    def delete_head(self):
        """Delete first element"""
        pass

    def search(self):
        """Return given element"""
        pass

    def is_empty(self):
        """Checks if list is empty"""
        pass


if __name__ == '__name__':
    head_node = Node(1)
    linked_list = LinkedList(head_node)
    print(f'linked_list -> {linked_list}')
