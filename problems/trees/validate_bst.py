class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def validate_bst(root: TreeNode, low=float('-inf'), high=float('inf')) -> bool:
    if not root:
        return True

    if not low < root.val < high:
        return False

    return validate_bst(root.left, low, min(root.val, high)) and \
        validate_bst(root.right, max(low, root.val), high)


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
    result = validate_bst(root)
    print(f'result -> {result}')
