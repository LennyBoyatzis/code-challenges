def memoize(fn):
    cache = {}

    def inner_fn(n):
        if n not in cache:
            cache[n] = fn(n)
            return cache[n]
        return fn(n)
    return inner_fn


@memoize
def climb_stairs(n: int) -> int:
    if n < 2:
        return 1

    return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs_dp(n: int) -> int:
    options = [1, 2]

    for i in range(2, n):
        next_val = options[i - 2] + options[i - 1] + 2
        options.append(next_val)

    return options[-1]


if __name__ == '__main__':
    result = climb_stairs_dp(35)
    print(f'what is the result {result}')
