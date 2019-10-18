from typing import List


def reverse(x: int) -> int:
    max_int = 2**31 - 1
    min_int = -2**31
    reversed_x = None

    if x < 0:
        x = x * -1
        str_x = '-' + str(x)[::-1]
        reversed_x = int(str_x)
    else:
        str_x = str(x)[::-1]
        reversed_x = int(str_x)

    if reversed_x > max_int:
        return 0
    elif reversed_x < min_int:
        return 0

    return reversed_x


if __name__ == '__main__':
    result = reverse(-123)
    print(f'result after: {result}')
