def memoize(fn):
    cache = {}

    def inner(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    return inner


@memoize
def fib(n):
    print(f'number of times running {n}')
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    result = fib(5)
    print(f'here is the result {result}')
