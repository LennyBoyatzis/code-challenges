from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order_traversal(root: TreeNode, output: List[int]) -> List[int]:
    if root is None:
        return []

    output.append(root.val)

    if root.left:
        pre_order_traversal(root.left, output)

    if root.right:
        pre_order_traversal(root.right, output)

    return output


def in_order_traversal(root: TreeNode, output: List[int]) -> List[int]:
    if root is None:
        return []

    if root.left:
        in_order_traversal(root.left, output)

    output.append(root.val)

    if root.right:
        in_order_traversal(root.right, output)

    return output


def post_order_traversal(root: TreeNode, output: List[int]) -> List[int]:
    if root is None:
        return []

    if root.left:
        post_order_traversal(root.left, output)

    if root.right:
        post_order_traversal(root.right, output)

    output.append(root.val)

    return output


if __name__ == '__main__':
    t_0 = TreeNode(7)
    t_1 = TreeNode(3)
    t_2 = TreeNode(11)
    t_3 = TreeNode(1)
    t_4 = TreeNode(5)
    t_5 = TreeNode(9)
    t_6 = TreeNode(13)
    t_7 = TreeNode(0)
    t_8 = TreeNode(2)
    t_9 = TreeNode(4)
    t_10 = TreeNode(6)
    t_11 = TreeNode(8)
    t_12 = TreeNode(10)
    t_13 = TreeNode(12)
    t_14 = TreeNode(14)

    # Root
    t_0.left = t_1
    t_0.right = t_2

    # 1st Level
    t_1.left = t_3
    t_1.right = t_4

    t_2.left = t_5
    t_2.right = t_6

    # 2nd Level
    t_3.left = t_7
    t_3.right = t_8

    t_4.left = t_9
    t_4.right = t_10

    t_5.left = t_11
    t_5.right = t_12

    t_6.left = t_13
    t_6.right = t_14

    output = []

    result = post_order_traversal(t_0, output)
    print(f'what is the result {result}')
