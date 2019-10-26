class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric(node1: TreeNode, node2: TreeNode) -> bool:
    if not node1 and not node2:
        return True

    if not node1 or not node2:
        return False

    return ((node1.val == node2.val)
            and is_symmetric(node1.right, node2.left)
            and is_symmetric(node1.left, node2.right))


if __name__ == '__main__':
    root = TreeNode(5)
    two = TreeNode(1)
    three = TreeNode(6)
    four = TreeNode(3)
    five = TreeNode(9)

    root.left = two
    root.right = three

    three.left = four
    three.right = five
    result = is_symmetric(root, root)
    print(f'result -> {result}')
