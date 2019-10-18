class Stack():
    def __init__(self):
        self.store = []

    def push(self, value: int) -> None:
        """Add element to the top of the stack"""
        self.store.append(value)

    def pop(self) -> int:
        """Remove and return element from the top of the stack"""
        return self.store.pop()

    def peek(self) -> int:
        """Read value from top of the stack"""
        return self.store[-1]

    def is_empty(self) -> bool:
        """Checks is stack is empty"""
        return len(self.store) == 0


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(2)
    stack.push(3)
    element = stack.pop()
    print(f'element {element}')
