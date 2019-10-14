from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left != right:
        min_height = min(height[left], height[right])
        width = right - left
        area = min_height * width
        max_area = max(max_area, area)

        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1

    return max_area


if __name__ == '__main__':
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area(heights)
    print(f'result -> {result}')
