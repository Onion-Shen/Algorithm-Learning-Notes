from typing import List, Any


class ListGraphyNode(object):
    def __init__(self, data: Any):
        self.nextarc: ListGraphyNode = None
        self.data: Any = data


class ListGraphy(object):
    def __init__(self):
        self.Adj: List[ListGraphyNode] = None


class MatrixGraphy(object):
    def __init__(self):
        self.matrix: List[List[int]] = None
