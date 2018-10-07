
from typing import Any


class Node(object):
    def __init__(self, key: Any):
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.key: Any = key

    def minimum(self):
        """
        :rtype: Node
        """
        tmp = self
        while tmp.left:
            tmp = tmp.left
        return tmp

    def maximum(self):
        """
        :rtype: Node
        """
        tmp = self
        while tmp.right:
            tmp = tmp.right
        return tmp

    def search(self, k: Any):
        """
        :rtype: Node
        """
        x = self
        while x and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def successor(self):
        """
        :rtype: Node
        """
        tmp = self
        if tmp.right:
            return tmp.right.minimum()

        y = tmp.parent
        while y and tmp == y.right:
            tmp = y
            y = y.parent

        return y


class BST(object):
    def __init__(self):
        self.root: Node = None

    def insert(self, z: Node):
        y: Node = None
        x = self.root
        while x:
            y = x
            x = x.left if z.key < x.key else x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u: Node, v: Node):
        """
            use a tree root by v replace a tree root by u
        """
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v:
            v.parent = u.parent

    def delete(self, z: Node):
        if not z.left:
            self.transplant(z, z.right)
        elif not z.right:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y