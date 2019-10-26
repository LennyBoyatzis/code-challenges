from functools import wraps


def trace(func):
    func_name = func.__name__
    separator = '|  '
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        trace.recursion_depth -= 1
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func
