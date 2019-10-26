from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums2_index = 0

    for index, num1_val in enumerate(nums1):
        if nums2_index < n - 1:
            if nums2[nums2_index] == num1_val:
                nums1[(m + index) - 1] = nums1[index + 1]
                nums1[index + 1] = nums2[nums2_index]
                nums2_index += 1
            elif nums2[nums2_index] < num1_val:
                nums1[(m + index) - 1] = nums1[index]
                nums1[index] = nums2[nums2_index]
                nums2_index += 1
        elif nums2_index == n - 1:
            nums1[-1] = nums2[nums2_index]

    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    result = merge(nums1, 3, nums2, 3)
    print(f'result -> {result}')
