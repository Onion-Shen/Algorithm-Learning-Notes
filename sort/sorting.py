# implementation of sorting algorithm

from typing import List, Any, Callable
from dataStructure.heap import make_heap, heapify
from math import floor


def insertion_sort(array: List[Any], cmp: Callable[[Any, Any], bool]):
    """
        insertion sort O(n^2)
    """
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and cmp(array[i], key):
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


def heap_sort(heap: List[Any], cmp: Callable[[Any, Any], bool]) -> List[Any]:
    """
        heap sort O(nlgn)
    """
    tmp = list(heap)
    make_heap(tmp, cmp)
    sorted_array = []
    while tmp:
        top = tmp.pop(0)
        sorted_array.append(top)
        heapify(tmp, 0, cmp)
    return sorted_array


def counting_sort(array: List[Any], k: int) -> List[Any]:
    """
        counting sort O(k + n)
        k: max item in array
    """
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
    """
        merge sort O(nlgn)
    """
    if start < end:
        middle = floor((start + end) / 2)
        merge_sort(array, start, middle, cmp)
        merge_sort(array, middle + 1, end, cmp)
        merge(array, start, middle, end, cmp)


def partition(array: List[Any], p: int, r: int, cmp: Callable[[Any, Any], bool]) -> int:
    # O(n) (n = r - p + 1)
    pivot = array[r]
    i = p - 1
    for j in range(p, r):
        if cmp(array[j], pivot):
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array: List[Any], p: int, r: int, cmp: Callable[[Any, Any], bool]):
    """
        quick sort O(nlgn)
    """
    if p < r:
        q = partition(array, p, r, cmp)
        quick_sort(array, p, q - 1, cmp)
        quick_sort(array, q + 1, r, cmp)
