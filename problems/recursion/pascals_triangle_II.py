from typing import List

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


def calculate_item(row: int, col: int) -> List[int]:
    if col == 1 or row == col:
        return 1

    return calculate_item(row - 1, col - 1) + calculate_item(row - 1, col)


# We know row will start or end with 1

def get_row(rowIndex: int) -> List[int]:
    if rowIndex == 1:
        return [1, 1]


if __name__ == '__main__':
    result = calculate_item(5, 3)
    print(f'result -> {result}')
