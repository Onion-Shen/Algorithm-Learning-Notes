# quick sort O(nlgn)

from typing import List, Any, Callable


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
    if p < r:
        q = partition(array, p, r, cmp)
        quick_sort(array, p, q - 1, cmp)
        quick_sort(array, q + 1, r, cmp)
