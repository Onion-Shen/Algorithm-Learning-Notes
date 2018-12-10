from typing import List


class ArcNode(object):
    def __init__(self, adjvex: int, nextarc: ArcNode):
        self.adjvex = adjvex
        self.nextarc = nextarc


class VexNode(object):
    def __init__(self, vertex: int, firstarc: ArcNode):
        self.vertex = vertex
        self.firstarc = firstarc


class ListGraphy(object):
    def __init__(self, vexnum: int, arcnum: int):
        self.adjlist: List[VexNode] = []
        self.vexnum = vexnum
        self.arcnum = arcnum
        for i in range(vexnum):
            head = VexNode(i, None)
            self.adjlist.append(head)
