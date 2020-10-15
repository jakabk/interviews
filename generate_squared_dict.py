# With a given number n, write a function that generates a dictionary containing key-value pairs
# where the key is a number and the value is the square of that number.
# The input number n is between 1 and n (both included). and then the function should return the dictionary.

# Example:
# >>> generate_squared_dict(8)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
import json
from typing import Dict


def generate_squared_dict(n: int) -> Dict[int, int]:
    return {
        i: i * i for i in range(1, n + 1)
    }


if __name__ == "__main__":
    assert json.dumps(generate_squared_dict(8), sort_keys = True) == \
           json.dumps({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}, sort_keys = True)
