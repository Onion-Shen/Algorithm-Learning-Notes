from typing import List


class ArcNode(object):
    def __init__(self, adjvex: int, nextarc):
        self.adjvex = adjvex
        self.nextarc: ArcNode = nextarc


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
            # i means the index of vertex
            head = VexNode(i, None)
            self.adjlist.append(head)

        for _ in range(arcnum):
            # indexes between a arc
            i, j = map(lambda x: int(x), input("i,j = ").split(","))

            pe = ArcNode(j, self.adjlist[i].firstarc)
            self.adjlist[i].firstarc = pe

            pb = ArcNode(i, self.adjlist[j].firstarc)
            self.adjlist[j].firstarc = pb
