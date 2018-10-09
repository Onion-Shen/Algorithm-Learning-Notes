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
        if head == self.dummy:
            head.next = node
            node.prev = head
        else:
            prev = head.prev
            prev.next = node
            node.prev = prev
            node.next = head

    def head(self) -> Node:
        return self.dummy.next

    def search(self, key: Any) -> Node:
        tmp = self.dummy
        while tmp:
            if tmp.key == key:
                return tmp
            tmp = tmp.next
        return None

    def delete(self, key: Any):
        tmp = self.dummy
        while tmp and tmp.key != key:
            tmp = tmp.next
        self.deleteNode(tmp)

    def deleteNode(self, node: Node):
        if not node:
            return

        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def exchange(self, node1: Node, node2: Node):
        if node1 == node2:
            return

        prev1, next1 = node1.prev, node1.next
        prev2, next2 = node2.prev, node2.next

        prev1.next = node2
        node2.next = next1

        prev2.next = node1
        node1.next = next2

        node1.prev = prev2
        node1.next = next2

        node2.prev = prev1
        node2.next = next1

    def clear(self):
        self.dummy.next = None

    def __str__(self):
        head = self.head()
        if head == self.dummy:
            return None

        array = []
        while head:
            array.append(head.key.__str__())
            head = head.next
        return ",".join(array)
