def climb_stairs(n: int) -> int:
    if n == 1:
        return 1

    num_ways = [0] * n
    num_ways[0], num_ways[1] = 1, 2

    for i in range(2, n):
        num_ways[i] = num_ways[i - 1] + num_ways[i - 2]

    return num_ways[-1]


if __name__ == '__main__':
    result = climb_stairs(6)
    print(f'result {result}')
