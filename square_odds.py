# Use a list comprehension to square each odd number in a string separated by commas. The function should return a list of integers.
# Example:
# >>> square_odds('1,2,3,4,5,6,7,8,9')
# [1, 9, 25, 49, 81]
from typing import List


def square_odds(numbers: str) -> List[int]:
    return [odd ** 2 for odd in map(int, numbers.split(",")) if bool(odd % 2)]


if __name__ == "__main__":
    assert square_odds('1,2,3,4,5,6,7,8,9') == [1, 9, 25, 49, 81]
    print(square_odds('1,2,3,4,5,6,7,8,9'))
