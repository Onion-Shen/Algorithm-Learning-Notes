from typing import Any
from dataStructure.binarySearchTree import Node


class AVLNode(Node):
    def __init__(self, key: Any):
        Node.__init__(self, key)
        self.depth = 0

    def update_depth(self):
        self.depth = max(self.left_depth(), self.right_depth()) + 1

    def left_depth(self) -> int:
        return self.left.depth if self.left else 0

    def right_depth(self) -> int:
        return self.right.depth if self.right else 0

    def __str__(self) -> str:
        return str(self.key)


def ll_rotation(node: AVLNode) -> AVLNode:
    if node is None:
        return None

    left = node.left
    node.left = left.right
    left.right = node

    node.update_depth()
    left.update_depth()

    return left


def rr_rotation(node: AVLNode) -> AVLNode:
    if node is None:
        return None

    right = node.right
    node.right = right.left
    right.left = node

    node.update_depth()
    right.update_depth()

    return right


def lr_rotation(node: AVLNode) -> AVLNode:
    if node is None:
        return None

    node.left = rr_rotation(node.left)
    return ll_rotation(node)


def rl_rotation(node: AVLNode) -> AVLNode:
    if node is None:
        return None

    node.right = ll_rotation(node.right)
    return rr_rotation(node)


class AVLTree(object):
    def __init__(self):
        self.root: AVLTree = None

    def __insert_node(self, tree: AVLNode, key: Any) -> AVLNode:
        if tree is None:
            tree = AVLNode(key)
        elif key < tree.key:
            tree.left = self.__insert_node(tree.left, key)
            if tree.left_depth() - tree.right_depth() == 2:
                if key < tree.left.key:
                    tree = ll_rotation(tree)
                else:
                    tree = lr_rotation(tree)
        elif key > tree.key:
            tree.right = self.__insert_node(tree.right, key)
            if tree.right_depth() - tree.left_depth() == 2:
                if key > tree.right.key:
                    tree = rr_rotation(tree)
                else:
                    tree = rl_rotation(tree)

        tree.update_depth()
        return tree

    def insert(self, key: Any):
        if self.root is None:
            self.root = AVLNode(key)
            return
        self.root = self.__insert_node(self.root, key)

    def __delete_node(self, tree: AVLNode, z: AVLNode) -> AVLNode:
        if tree is None or z is None:
            return None

        if z.key < tree.key:
            tree.left = self.__delete_node(tree.left, z)
            if tree.right_depth() - tree.left_depth() == 2:
                r: AVLNode = tree.right
                if r.left_depth() > r.right_depth():
                    tree = rl_rotation(tree)
                else:
                    tree = rr_rotation(tree)
        elif z.key > tree.key:
            tree.right = self.__delete_node(tree.right, z)
            if tree.left_depth() - tree.right_depth() == 2:
                l: AVLNode = tree.left
                if l.right_depth() > l.left_depth():
                    tree = lr_rotation(tree)
                else:
                    tree = ll_rotation(tree)
        else:
            if tree.left and tree.right:
                if tree.left_depth() > tree.right_depth():
                    max_node = tree.left.maximum()
                    tree.key = max_node.key
                    tree.left = self.__delete_node(tree.left, max_node)
                else:
                    min_node = tree.right.minimum()
                    tree.key = min_node.key
                    tree.right = self.__delete_node(tree.right, min_node)
            else:
                tree = tree.left if tree.left else tree.right

        return tree

    def delete(self, key: Any):
        node = self.search(key)
        if node is None:
            return

        self.__delete_node(self.root, node)

    def search(self, key: Any) -> AVLNode:
        if key is None or self.root is None:
            return None

        return self.root.search(key)
