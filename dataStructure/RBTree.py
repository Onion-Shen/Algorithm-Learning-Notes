
from typing import Any
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class Node(object):
    def __init__(self, key: Any, color: Color):
        self.key: Any = key
        self.color: Color = color
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None

    def minimum(self):
        """
        :rtype: Node
        """
        tmp = self
        while tmp.left:
            tmp = tmp.left
        return tmp

    def search(self, k: Any):
        """
        :rtype: Node
        """
        x = self
        while x and k != x.key:
            x = x.left if k < x.key else x.right
        return x


"""
rules:
    1.Each node is either red or black.
    2.The root is black. 
    3.All leaves (NIL) are black.
    4.If a node is red, then both its children are black.
    5.Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
"""


class RBTree(object):
    def __init__(self):
        self.root: Node = None
        self.leaf: Node = Node(None, Color.BLACK)

    def left_rotate(self, node: Node):
        y = node.right
        node.right = y.left

        if y.left != self.leaf:
            y.left.parent = node
        y.parent = node.parent

        if node.parent == self.leaf:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node: Node):
        y = node.left
        node.left = y.right

        if y.right != self.leaf:
            y.right.parent = node
        y.parent = node.parent

        if node.parent == self.leaf:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node
        node.parent = y

    def insert(self, node: Node):
        y = self.leaf
        x = self.root

        while x != self.leaf:
            y = x
            x = x.left if node.key < x.key else x.right
        node.parent = y

        if y == self.leaf:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.left = self.leaf
        node.right = self.leaf
        node.color = Color.RED

        self.insert_fixup(node)

    def insert_fixup(self, node: Node):
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right

                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                elif node == node.parent.right:
                    node = node.parent
                    self.left_rotate(node)

                node.parent.color = Color.BLACK
                node.parent.parent.color = Color.RED
                self.right_rotate(node.parent.parent)
            elif node.parent == node.parent.parent.right:
                y = node.parent.parent.left

                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                elif node == node.parent.left:
                    node = node.parent
                    self.right_rotate(node)

                node.parent.color = Color.BLACK
                node.parent.parent.color = Color.RED
                self.left_rotate(node.parent.parent)
                

        self.root.color = Color.BLACK

    def transplant(self, u: Node, v: Node):
        if u.parent == self.leaf:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete(self, node):
        pass

    def delete_fixup(self, node):
        pass
