from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


@memoize
def climb_stairs(i: int, n: int) -> int:
    if i > n:
        return 0
    elif i == n:
        return 1

    return climb_stairs(i + 1, n) + climb_stairs(i + 2, n)


if __name__ == '__main__':
    result = climb_stairs(0, 5)
    print(f'result {result}')
