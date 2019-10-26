class MinStack:
    def __init__(self):
        self.store = []

    def push(self, x: int) -> None:
        current_min = min(self.get_min(), x)
        self.store.append((x, current_min))

    def pop(self) -> None:
        self.store.pop()

    def top(self) -> int:
        if self.store:
            return self.store[-1][0]

    def get_min(self) -> int:
        if self.store:
            return self.store[-1][1]
        return float('inf')


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    min_stack.get_min()
    min_stack.pop()
    min_stack.top()
    min_val = min_stack.get_min()
    print(f'min_val {min_val}')
