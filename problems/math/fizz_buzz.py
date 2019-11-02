def fizz_buzz(n: int) -> None:
    outputs = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            outputs.append("FizzBuzz")
        elif i % 3 == 0:
            outputs.append("Fizz")
        elif i % 5 == 0:
            outputs.append("Buzz")
        else:
            outputs.append(f'{i}')
    return outputs


if __name__ == '__main__':
    n = 100
    result = fizz_buzz(n)
    print(f'result -> {result}')
