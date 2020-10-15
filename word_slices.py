# >>> word_slices('i')
# ['i']
# >>> word_slices('to')
# ['to']
# >>> word_slices('are')
# ['ar', 'are', 're']
# >>> word_slices('table')
# ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']
# Implement the word_slices function.
from typing import List


def word_slices(word: str) -> List[str]:
    if len(word) < 3:
        return [word]

    slices = []
    for i in range(len(word) - 1):
        for j in range(2, len(word) + 1):
            if i + j <= len(word):
                print(word, i, j, i + j, word[i:i + j])
                slices.append(word[i:i + j])

    print(slices)
    return slices


if __name__ == "__main__":
    assert word_slices('i') == ['i']
    assert word_slices('to') == ['to']
    assert word_slices('are') == ['ar', 'are', 're']
    assert word_slices('table') == ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']
