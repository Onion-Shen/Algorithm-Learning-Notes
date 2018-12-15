from typing import List
from dataStructure.linkedList import LinkedList


class ListGraphy(object):
    def __init__(self, vexnum: int):
        self.vexnum = vexnum
        self.adjList = [LinkedList() for _ in range(vexnum)]

    def add_edge(self, v: int, w: int):
        # add w to the list of node of v
        linkedlist = self.adjList[v]
        linkedlist.insert_tail(w)


class MatrixGraphy(object):
    def __init__(self, vexnum: int, arcnum: int):
        self.vexnum = vexnum
        self.arcnum = arcnum

        self.edge: List[List[int]] = [
            [1 if x == y else None for x in range(vexnum)] for y in range(vexnum)]

        for _ in range(arcnum):
            # index and weight of a arc
            i, j, w = map(lambda x: int(x), input("i,j,w = ").split(","))

            self.edge[i - 1][j - 1] = w
            self.edge[j - 1][i - 1] = w
