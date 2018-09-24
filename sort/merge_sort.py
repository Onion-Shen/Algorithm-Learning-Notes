# merge sort O(nlgn)

from typing import List
from typing import Any
from typing import Callable
from math import floor


def merge(array: List[Any], start: int, middle: int, end: int, cmp: Callable[[Any, Any], bool]):
    leftSize = middle - start + 1
    left = array[start:start + leftSize]

    rightSize = end - middle
    right = array[(middle + 1):(middle + 1) + rightSize]

    i, j, k = 0, 0, start

    while k <= end:
        leftItem = left[i] if i < leftSize else None
        rightItem = right[j] if j < rightSize else None
        if leftItem and rightItem:
            if cmp(leftItem, rightItem):
                array[k] = leftItem
                i += 1
            else:
                array[k] = rightItem
                j += 1
        else:
            if leftItem:
                array[k] = leftItem
                i += 1
            elif rightItem:
                array[k] = rightItem
                j += 1
        k += 1


def merge_sort(array: List[Any], start: int, end: int, cmp: Callable[[Any, Any], bool]):
    if start < end:
        middle = floor((start + end) / 2)
        merge_sort(array, start, middle, cmp)
        merge_sort(array, middle + 1, end, cmp)
        merge(array, start, middle, end, cmp)
