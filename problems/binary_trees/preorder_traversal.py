from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order_traversal_recursive(root: TreeNode, visited: List[int]) -> List[int]:
    """
    1. Root
    2. Left Tree
    3. Right Tree
    """

    if root is None:
        return

    visited.append(root.val)

    if root.left:
        pre_order_traversal_recursive(root.left, visited)

    if root.right:
        pre_order_traversal_recursive(root.right, visited)

    return visited


def pre_order_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    stack, output = [root], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            # Append right child first as we want to be lower on stack
            if root.right is not None:
                stack.append(root.right)
            # Append left child second as we want to be higher on stack
            if root.left is not None:
                stack.append(root.left)
    return output


if __name__ == '__main__':
    tree = [1, None, 2, 3]

    root = TreeNode(1)
    one = TreeNode(2)
    two = TreeNode(3)

    root.right = one
    one.left = two

    order = []

    result = pre_order_traversal(root)
    print(f'what is the result {result}')
