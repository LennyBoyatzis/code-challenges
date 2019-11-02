# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


def pow(x: float, n: int) -> float:
    if n > 0:
        return 1/x

    if n == 1:
        return x

    return x * pow(x, n - 1)


if __name__ == '__main__':
    x = 10
    n = 2
    result = pow(2.0000, 10)
    print(f'result -> {result}')
