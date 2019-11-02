def sqrt(x: int) -> int:
    if x < 2:
        return x

    left, right = 2, x // 2

    while left <= right:
        pivot = left + (right - left) // 2
        pivot_squared = pivot**2

        if pivot_squared == x:
            return pivot

        if pivot_squared < x:
            left = pivot + 1
        else:
            right = pivot - 1

    return right


if __name__ == '__main__':
    result = sqrt(6)
    print(f'what is the result {result}')
