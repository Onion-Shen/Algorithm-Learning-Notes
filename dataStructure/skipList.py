from typing import Any, List
from random import random


class SkipNode(object):
    DEFAULT_SIZE = 100

    def __init__(self, size: int = DEFAULT_SIZE, data: Any = None):
        self.data: Any = data
        self.link: List[SkipNode] = [None] * size


class SkipList(object):
    P = 0.25

    def __init__(self, tail_data: Any, max_level: int):
        self.max_level = max_level
        self.level = 0

        self.tail = SkipNode(0, tail_data)

        number_of_level = max_level + 1
        self.head = SkipNode(number_of_level)
        for i in range(number_of_level):
            self.head.link[i] = self.tail

        self.pre_nodes: List[SkipNode] = [None] * number_of_level

    def __str__(self):
        rows = []

        for i in range(self.level, -1, -1):
            node = self.head.link[i]

            row = []
            while node != None and node.data < self.tail.data:
                row.append(str(node.data))
                node = node.link[i]

            rows.append("-".join(row) if row else "")

        return "\n".join(rows)

    def search(self, key: Any) -> bool:
        if key == None or key >= self.tail.data:
            return False

        node = self.head
        for i in range(self.level, -1, -1):
            while node.link[i].data < key:
                node = node.link[i]
        return node.link[0].data == key

    def random_level(self) -> int:
        cnt = 0
        while cnt < self.max_level and random() < self.P:
            cnt += 1
        return cnt

    def update_pre_nodes(self, key: Any) -> SkipNode:
        if key == None or key >= self.tail.data:
            return None

        node = self.head
        for i in range(self.level, -1, -1):
            while node.link[i].data < key:
                node = node.link[i]
            self.pre_nodes[i] = node

        return node.link[0]

    def remove(self, el: Any) -> bool:
        node = self.update_pre_nodes(el)
        if node == None or node == self.tail:
            return False

        i = 0
        while i <= self.level and self.pre_nodes[i].link[i].data == el:
            self.pre_nodes[i].link[i] = node.link[i]
            i += 1

        while self.level > 0 and self.head.link[self.level] == self.tail:
            self.level -= 1

        return True

    def insert(self, el: Any) -> bool:
        node = self.update_pre_nodes(el)
        if node == None or node.data == el:
            return False

        if self.random_level() > self.level:
            self.level += 1
            self.pre_nodes[self.level] = self.head

        new_node = SkipNode(self.level + 1, el)
        for i in range(self.level, -1, -1):
            new_node.link[i] = self.pre_nodes[i].link[i]
            self.pre_nodes[i].link[i] = new_node

        return True
