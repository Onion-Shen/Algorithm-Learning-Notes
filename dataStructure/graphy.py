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


def BFS(graphy: ListGraphy, source: int):
    visited = [False] * graphy.vexnum
    queue: List[int] = list()

    visited[source] = True
    queue.append(source)

    while queue:
        s = queue.pop(0)
        print(s)

        linkedlist = graphy.adjList[s]
        head = linkedlist.dummy.next

        while head:
            k = head.key
            if not visited[k]:
                visited[k] = True
                queue.append(k)
            head = head.next


def DFS(graphy: ListGraphy, source: int):
    def DFS_visit(graphy: ListGraphy, source: int, visited: List[bool]):
        visited[source] = True
        print(source)

        linkedlist = graphy.adjList[source]
        head = linkedlist.dummy.next

        while head:
            k = head.key
            if not visited[k]:
                DFS_visit(graphy, k, visited)
            head = head.next

    visited = [False] * graphy.vexnum
    DFS_visit(graphy, source, visited)
