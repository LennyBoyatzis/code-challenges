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


def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split(' ')

    for token in tokens:
        if token.isdigit():
            stack.push(token)
        elif token == '+':
            num_one = stack.pop()
            num_two = stack.pop()
            result = int(num_one) + int(num_two)
            stack.push(result)
        elif token == '*':
            num_one = stack.pop()
            num_two = stack.pop()
            result = int(num_one) * int(num_two)
            stack.push(result)
    print(f'tokens {tokens}')


if __name__ == '__main__':
    expression = '56 47 + 2 *'
    result = evaluate_postfix(expression)
    print(f'result -> {result}')
