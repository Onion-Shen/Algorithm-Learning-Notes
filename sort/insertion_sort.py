# insertion sort

from typing import List
from typing import Any
from typing import Callable


def insertion_sort(array: List[Any], cmp: Callable[[Any, Any], bool]):
    if not array or not cmp:
        return

    size = len(array)
    if size < 1:
        return

    for j in range(1, size):
        key = array[j]
        i = j - 1
        while i >= 0 and cmp(array[i], key):
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
