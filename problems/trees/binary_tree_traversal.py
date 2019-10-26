from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root: TreeNode, levels=[], level=0) -> List[List[int]]:
    if not root:
        return levels

    if len(levels) == level:
        levels.append([])

    levels[level].append(root.val)

    print(f'levels {levels}')

    if root.left:
        level_order(root.left, levels, level + 1)

    if root.right:
        level_order(root.right, levels, level + 1)

    return levels


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
    result = level_order(root)
    print(f'what is the result {result}')
