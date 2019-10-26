from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build(nums: List[int],
          low: int,
          high: int) -> TreeNode:

    if low == high:
        # root node
        return TreeNode(nums[low])
    elif low < high:
        mid = (low + high + 1) // 2
        node = TreeNode(nums[mid])
        node.left = build(nums, low, mid - 1)
        node.right = build(nums, mid + 1, high)
        return node


def convert_sorted_array_to_bst(nums: List[int]):
    return build(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    # nums = [-10, -3, 0, 5, 9]
    nums = [1, 2, 3, 4, 5, 6, 7]
    node = convert_sorted_array_to_bst(nums)
