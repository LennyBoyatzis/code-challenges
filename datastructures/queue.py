class Queue():
    def __init__(self):
        self.store = []

    def enqueue(self, val):
        """Add element to back of the queue"""
        self.store.append(val)

    def dequeue(self):
        """Remove and return element from front of queue"""
        return self.store.pop(0)

    def top(self):
        """Read element from front of queue"""
        return self.store[0]

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.store) == 0


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    element = queue.dequeue()
    print(f'element {element}')
