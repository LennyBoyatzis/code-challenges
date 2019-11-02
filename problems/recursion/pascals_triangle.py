from typing import List

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


def generate(numRows: int) -> List[List[int]]:
    triangle = []

    for row_num in range(numRows):
        row = [None for _ in range(row_num+1)]
        row[0], row[1] = 1, 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1]


if __name__ == '__main__':
    result = generate(5)
    print(f'what is the result -> {result}')
