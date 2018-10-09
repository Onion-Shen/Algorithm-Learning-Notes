from typing import Any


class Node(object):
    def __init__(self, key: Any):
        self.key: Any = key
        self.prev: Node = None
        self.next: Node = None


class LinkedList(object):
    def __init__(self):
        self.dummy = Node(None)

    def insert_tail(self, key: Any):
        node = Node(key)
        tail = self.tail()
        tail.next = node
        node.prev = tail

    def tail(self) -> Node:
        tmp = self.dummy
        while tmp.next:
            tmp = tmp.next
        return tmp

    def insert_head(self, key: Any):
        node = Node(key)

        head = self.head()
        if not head:
            self.dummy.next = node
            node.prev = self.dummy
            return

        prev = head.prev
        if prev:
            prev.next = node
        head.prev = node

        node.prev, node.next = prev, head

    def head(self) -> Node:
        return self.dummy.next

    def search(self, key: Any) -> Node:
        head = self.head()
        while head and head.key != key:
            head = head.next
        return head

    def delete(self, key: Any):
        node = self.search(key)
        self.deleteNode(node)

    def deleteNode(self, node: Node):
        if not node:
            return

        prev, next = node.prev, node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

    def exchange(self, node1: Node, node2: Node):
        if node1 == node2:
            return

        prev1, next1 = None, None
        if node1:
            prev1, next1 = node1.prev, node1.next

        prev2, next2 = None, None
        if node2:
            prev2, next2 = node2.prev, node2.next

        if node1:
            node1.prev, node1.next = prev2, next2

        if node2:
            node2.prev, node2.next = prev1, next1

        if prev1:
            prev1.next = node2
        if prev2:
            prev2.next = node1

        if next1:
            next1.prev = node2
        if next2:
            next2.prev = node1

    def clear(self):
        self.dummy.next = None

    def __str__(self) -> str:
        head = self.head()
        if not head:
            return None

        array = []
        while head:
            array.append(head.key)
            head = head.next

        return array.__str__()
