actual_versions = [False] * 100 + [True] * 10


def is_bad_version(n: int) -> bool:
    return actual_versions[n - 1]


# Binary Search
def first_bad_version(n: int) -> int:
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    versions = 110
    result = first_bad_version(versions)
    print(f'result -> {result}')
