from functools import wraps


def trace(func):
    func_name = func.__name__
    separator = '|  '
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        trace.recursion_depth -= 1
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    root = TreeNode(3)
    two = TreeNode(9)
    three = TreeNode(20)
    four = TreeNode(15)
    five = TreeNode(7)

    root.left = two
    root.right = three

    three.left = four
    three.right = five
    max_depth = trace(max_depth)
    result = max_depth(root)
    print(f'result -> {result}')
