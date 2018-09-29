# find maximum subarray O(nlgn)

from typing import List
from typing import Any
from typing import Tuple
from math import floor


def find_max_crossing_subarray(array: List[Any], low: int, mid: int, high: int) -> Tuple[int, int, int]:
    left_sum: int = None
    max_left: int = None
    Sum = 0
    for i in range(mid, low - 1, -1):
        Sum += array[i]
        if not left_sum or Sum > left_sum:
            left_sum = Sum
            max_left = i

    right_sum: int = None
    max_right: int = None
    Sum = 0
    for j in range(mid + 1, high + 1):
        Sum += array[j]
        if not right_sum or Sum > right_sum:
            right_sum = Sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(array: List[Any], low: int, high: int) -> Tuple[int, int, int]:
    if high == low:
        return (low, high, array[low])
    else:
        mid = floor((low + high) * 0.5)

        tuple_left = find_maximum_subarray(array, low, mid)
        tuple_right = find_maximum_subarray(
            array, mid + 1, high)
        tuple_cross = find_max_crossing_subarray(
            array, low, mid, high)

        max_sum = max(tuple_left[2], tuple_right[2], tuple_cross[2])
        if max_sum == tuple_left[2]:
            return tuple_left
        elif max_sum == tuple_right[2]:
            return tuple_right
        else:
            return tuple_cross
