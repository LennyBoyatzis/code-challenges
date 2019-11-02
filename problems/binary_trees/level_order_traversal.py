from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def breadth_first_search(root: TreeNode) -> List[List[int]]:
    queue, output = deque([root]), []
    level = 0

    while queue:
        node = queue.popleft()
        if output[level]:
            output[level] = output[level].append(node.val)

        output.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
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

    result = breadth_first_search(t_0)
