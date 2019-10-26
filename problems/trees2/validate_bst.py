class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_valid(root: TreeNode, low=float('-inf'), high=float('inf')) -> bool:
    if not root:
        return True

    if not low < root.val < high:
        return False

    return is_valid(root.left, low, min(root.val, high)) and \
        is_valid(root.right, max(low, root.val), high)


if __name__ == '__main__':
    root = TreeNode(2)
    two = TreeNode(1)
    three = TreeNode(3)

    root.left = two
    root.right = three

    result = is_valid(root)
    print(f'result -> {result}')
