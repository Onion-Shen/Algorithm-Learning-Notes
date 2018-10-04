# counting sort O(k + n)

from typing import List, Any


def counting_sort(array: List[Any], k: int) -> List[Any]:
    c = [0] * (k + 1)

    for j in array:
        c[j] += 1

    for j in range(1, len(c)):
        c[j] += c[j - 1]

    size = len(array)
    result = [None] * size

    for j in range(size - 1, -1, -1):
        a = array[j]
        result[c[a] - 1] = a
        c[a] -= 1

    return result
