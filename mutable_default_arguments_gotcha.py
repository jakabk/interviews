# https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

# What’s the output of this code:
def f(x, l = []):
    for i in range(x):
        l.append(i * i)
    # print(l)
    return l


if __name__ == "__main__":
    # >>> f(2)
    # ...
    assert f(2) == [0, 1]

    # >>> f(3,[3,2,1])
    # ...
    assert f(3, [3, 2, 1]) == [3, 2, 1, 0, 1, 4]

    # >>> f(3)
    # ...
    assert f(3) == [0, 1, 0, 1, 4]
