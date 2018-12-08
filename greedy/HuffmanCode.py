from dataStructure.binarySearchTree import Node
from typing import List, Dict, Tuple


class HuffmanTreeNode(Node):
    def __init__(self, key: str = None, weight: int = None):
        Node.__init__(self, key)
        self.weight = weight


def HuffmanEncode(data: List[HuffmanTreeNode]) -> Tuple[HuffmanTreeNode, Dict[str, str]]:
    sorted_data = sorted(data, key=lambda node: node.weight)

    while len(sorted_data) > 1:
        left = sorted_data.pop(0)
        right = sorted_data.pop(0)

        new_weight = left.weight + right.weight
        new_node = HuffmanTreeNode(None, new_weight)
        new_node.left = left
        new_node.right = right

        left.parent = new_node
        right.parent = new_node

        sorted_data.append(new_node)
        sorted_data.sort(key=lambda obj: obj.weight)

    head = sorted_data[0]

    codes = dict()
    for node in data:
        code: List[str] = []
        key = node.key
        while node.parent:
            if node.is_left_leaf():
                code.append("0")
            elif node.is_right_leaf():
                code.append("1")
            node = node.parent
        code.reverse()
        result = "".join(code)
        codes.setdefault(key, result)

    return head, codes
