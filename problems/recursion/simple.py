def simple_recursion(n: int) -> int:
    if n == 0:
        return 1

    return n + simple_recursion(n - 1)


if __name__ == '__main__':
    test = 10
    result = simple_recursion(test)
    print(f'Result -> {result}')
