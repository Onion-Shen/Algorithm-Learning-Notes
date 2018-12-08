from typing import List, Any, Dict


class ListGraphyNode(object):
    def __init__(self, data: Any):
        self.nextarc: ListGraphyNode = None
        self.data: Any = data
        self.visit = False

    def adjecent(self) -> List:
        adj_array = []
        head = self.nextarc
        while head:
            adj_array.append(head)
            head = head.nextarc
        return adj_array


class ListGraphy(object):
    def __init__(self):
        self.Adj: List[ListGraphyNode] = []

    def vertexs(self) -> List[ListGraphyNode]:
        vertex_array = []

        for node in self.Adj:
            while node:
                vertex_array.append(node)
                node = node.nextarc

        return vertex_array


class MatrixGraphy(object):
    def __init__(self):
        self.matrix: List[List[int]] = None


def dfs(graphy: ListGraphy):
    head = graphy.Adj[0]
    print(head.data)
    head.visit = True
    stack = [head]
    
    while stack:
        top = stack[-1]
        idx = 0
        adj_array = top.adjecent()

        for v in adj_array:
            if not v.visit:
                print(v.data)
                v.visit = True
                stack.append(v)
                break
            idx += 1

        if idx == len(adj_array):
            stack.pop()


def bfs(graphy: ListGraphy):
    head = graphy.Adj[0]
    isVisit: Dict[ListGraphyNode, bool] = {head: True}
    queue: List[ListGraphyNode] = [head]
    print(head.data)

    while queue:
        front = queue.pop(0)
        adj_array = front.adjecent()

        for node in adj_array:
            visit = isVisit.get(node)
            if not visit:
                print(node.data)
                queue.append(node)
                isVisit[node] = True
