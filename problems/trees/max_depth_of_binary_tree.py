from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth_recursion(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        left_height = max_depth_recursion(root.left)
        right_height = max_depth_recursion(root.right)
        return max(left_height, right_height) + 1


def max_depth_iterative(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([root, 0])

    while queue:
        node, level = queue.popleft()
        if node:
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return level


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
    # tree = [3, 9, 20, None, None, 15, 7]
    result = max_depth_recursion(root)
    print(f'result -> {result}')
