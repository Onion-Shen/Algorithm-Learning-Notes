from typing import Any, Dict
from dataStructure.linkedList import LinkedList,Node
from dataStructure.hashTable import Bucket


class LRUCache(object):
    def __init__(self, capacity: int):
        self.list: LinkedList = LinkedList()
        self.map: Dict[Any, Node] = dict()
        self.capacity = capacity

    def search(self, key: Any) -> Any:
        node = self.map.get(key)
        if not node:
            return None

        head = self.list.dummy.next
        self.list.exchange(head, node)

        return node.key.value

    def insert(self, key: Any, value: Any):
        node = self.map.get(key)
        if node:
            head = self.list.dummy.next
            self.list.exchange(head, node)
            node.key.value = value
        else:
            if len(self.map) == self.capacity:
                tail = self.list.tail()
                self.map.pop(tail.key.key)
                self.list.deleteNode(tail)

            self.list.insert_head(Bucket(key, value))
            self.map.setdefault(key, self.list.head())

    def clear(self):
        if self.list:
            self.list.clear()
        if self.map:
            self.map.clear()

    def contain(self, key: Any) -> bool:
        return self.map and self.map.get(key) != None

    def __str__(self) -> str:
        head = self.list.head()
        dic = {}
        while head:
            dic[head.key.key] = head.key.value
            head = head.next
        return dic.__str__()
