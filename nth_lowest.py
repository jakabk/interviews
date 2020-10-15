# >>> nums = [42, 23421341, 234.2e3, 21, 232, 12312, -2343]
# >>> nth_lowest(nums, 3)
# 42
# >>> nth_lowest(nums, 5)
# 12312
# >>> nth_lowest(nums)
# -2343
# Implement the nth_lowest function.
from typing import List


def nth_lowest(numbers: List[int], n: int = 1) -> int:
    return sorted(numbers)[n - 1]


if __name__ == "__main__":
    nums = [42, 23421341, 234.2e3, 21, 232, 12312, -2343]

    assert nth_lowest(nums, 3) == 42
    assert nth_lowest(nums, 5) == 12312
    assert nth_lowest(nums) == -2343
