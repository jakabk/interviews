# Implement the power decorator so that the output will be the following:
# @power(3)
# def add(a, b):
#     return a + b
#
# >>> add(2, 3)
# ... 125
# >>> add(1, 0)
# ... 1
# >>> add(5, 5)
# ... 1000

import functools


def power(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) ** n

        return wrapper

    return decorator


@power(3)
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(2, 3))
    assert add(2, 3) == 125

    print(add(1, 0))
    assert add(1, 0) == 1

    print(add(5, 5))
    assert add(5, 5) == 1000
