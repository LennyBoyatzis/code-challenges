from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def post_order_traversal(root: TreeNode, output: List[int]) -> List[int]:
    if root is None:
        return []

    if root.left is not None:
        post_order_traversal(root.left, output)

    if root.right is not None:
        post_order_traversal(root.right, output)

    output.append(root.val)
    return output


def post_order_traversal_iterative(root: TreeNode) -> List[int]:
    if root is None:
        return []

    stack, output = [root], []

    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)

    return output[::-1]


if __name__ == '__main__':
    tree = [0, 1, 2, 3, 4, 5, 6]

    root = TreeNode(0)
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    root.left = one
    root.right = two

    one.left = three
    one.right = four

    two.left = five
    two.right = six

    # output = []

    result = post_order_traversal_iterative(root)
    print(f'what is the result {result}')
