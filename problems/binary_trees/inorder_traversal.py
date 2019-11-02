from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_order_traversal_recursive(root: TreeNode, output: List[int]) -> List[int]:
    if root is None:
        return []

    if root.left is not None:
        in_order_traversal_recursive(root.left, output)

    output.append(root.val)

    if root.right is not None:
        in_order_traversal_recursive(root.right, output)

    return output


def in_order_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    stack, output = [root], []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        output.append(curr.val)
        curr = curr.right
    return output


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

    output = []

    result = in_order_traversal(root, output)
    print(f'what is the result {result}')
