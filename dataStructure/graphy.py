from typing import List
from sys import maxsize
from copy import deepcopy
from dataStructure.linkedList import LinkedList


class ListGraphy(object):
    def __init__(self, vexnum: int):
        self.vexnum = vexnum
        self.adjList = [LinkedList() for _ in range(vexnum)]
        self.indegrees = [0] * vexnum

    def add_edge(self, v: int, w: int):
        # add w to the list of node of v
        linkedlist = self.adjList[v]
        linkedlist.insert_tail(w)

        # change the indegree of vertex w
        self.indegrees[w] += 1


class MatrixGraphy(object):
    def __init__(self, vexnum: int, arcnum: int):
        self.vexnum = vexnum
        self.arcnum = arcnum

        self.matrix: List[List[int]] = [
            [0 if x == y else maxsize for x in range(vexnum)] for y in range(vexnum)]

    def add_edge(self, i: int, j: int, w: int):
        self.matrix[i][j] = w


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


def topological_sort(graphy: ListGraphy):
    queue: List[int] = list()
    for i in range(graphy.vexnum):
        if graphy.indegrees[i] == 0:
            queue.append(i)

    count = 0

    while queue:
        v = queue.pop(0)
        print(v)
        count += 1

        linkedlist = graphy.adjList[v]
        head = linkedlist.head()
        while head:
            key = head.key
            graphy.indegrees[key] -= 1
            if graphy.indegrees[key] == 0:
                queue.append(key)
            head = head.next

    if count < graphy.vexnum:
        print("there is a loop in the graphy")


def Floyd_Warshall_shortest_path(graphy: MatrixGraphy):
    vertex_num = graphy.vexnum
    matrix = deepcopy(graphy.matrix)

    for k in range(vertex_num):
        for i in range(vertex_num):
            for j in range(vertex_num):
                val = matrix[i][k] + matrix[k][j]
                if matrix[i][j] > val:
                    matrix[i][j] = val

    for row in matrix:
        print(row)
