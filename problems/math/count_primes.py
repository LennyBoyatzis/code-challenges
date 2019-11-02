def is_prime(n: int) -> bool:
    for i in range(n//2):
        if n % i == 0:
            return True
    return False


def count_primes(n: int) -> int:
    """Counts number of primes less than num n"""
    pass


if __name__ == '__main__':
    num = 10
    result = count_primes(10)
