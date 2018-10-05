from math import floor
from typing import List, Any, Callable


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
