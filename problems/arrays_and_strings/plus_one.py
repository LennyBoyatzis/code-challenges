from typing import List


def plus_one(digits: List[int]) -> int:
    for index in range(len(digits) - 1, -1, -1):
        if digits[index] is not 9:
            digits[index] = digits[index] + 1
            return digits
        else:
            digits[index] = 0
    return [1] + digits


if __name__ == '__main__':
    digits = [9, 9, 9]
    result = plus_one(digits)
    print(f'result -> {result}')
