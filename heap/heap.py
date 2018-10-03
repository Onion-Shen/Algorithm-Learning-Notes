# utility of operation in heap

from math import floor
from typing import List
from typing import Any
from typing import Callable


def PARENT(i: int) -> int:
    return floor(i / 2)


def LEFT(i: int) -> int:
    return i * 2 + 1


def RIGHT(i: int) -> int:
    return 2 * (i + 1)


def heapify(heap: List[Any], i: int, cmp: Callable[[Any, Any], bool]):
    size = len(heap)
    pivot = i

    left = LEFT(i)
    if left < size and cmp(heap[left], heap[pivot]):
        pivot = left

    right = RIGHT(i)
    if right < size and cmp(heap[right], heap[pivot]):
        pivot = right

    if pivot != i:
        heap[pivot], heap[i] = heap[i], heap[pivot]
        heapify(heap, pivot, cmp)


def make_heap(heap: List[Any], cmp: Callable[[Any, Any], bool]):
    size = int(len(heap)/2) - 1
    while size >= 0:
        heapify(heap, size, cmp)
        size -= 1


def heap_sort(heap: List[Any], cmp: Callable[[Any, Any], bool]) -> List[Any]:
    # heap sort O(nlgn)
    tmp = list(heap)
    make_heap(tmp, cmp)
    sorted_array = []
    while tmp:
        top = tmp.pop(0)
        sorted_array.append(top)
        heapify(tmp, 0, cmp)
    return sorted_array
