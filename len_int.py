# >>> len_int(96230)
# 5
# >>> len_int(-42)
# 3 <- It could be a mistake of the interviewer
# Implement the len_int function.
import math


def len_int(n: int) -> int:
    # return len(str(n))

    # minus_sign = 0
    if n < 0:
        n = n * -1
        # minus_sign = 1

    if n > 0:
        return int(math.log10(n)) + 1  # + minus_sign

    return 1


if __name__ == "__main__":
    assert len_int(96230) == 5
    assert len_int(-42) == 2
    assert len_int(0) == 1
