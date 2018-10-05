# heap sort O(nlgn)

from typing import List, Any, Callable
from dataStructure.heap import make_heap, heapify


def heap_sort(heap: List[Any], cmp: Callable[[Any, Any], bool]) -> List[Any]:
    tmp = list(heap)
    make_heap(tmp, cmp)
    sorted_array = []
    while tmp:
        top = tmp.pop(0)
        sorted_array.append(top)
        heapify(tmp, 0, cmp)
    return sorted_array
