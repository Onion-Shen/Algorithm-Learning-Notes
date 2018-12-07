from enum import Enum
from typing import Any, List


class ElemTag(Enum):
    Head = 0
    Atom = 1
    List = 2


class GLNode(object):
    def __init__(self, type: ElemTag, value: Any = None):
        self.type = type
        self.next: GLNode = None
        self.value: Any = value
        self.subLink: GLNode = None


class GLList(object):
    def __init__(self, content: str = None):
        chs: List[str] = list(content) if content and len(
            content) > 0 else None
        self.head = self.parse_content_to_list(chs)

    def parse_content_to_list(self, chs: List[str]) -> GLNode:
        if not chs or chs[0] != "(":
            return None

        chs.pop(0)

        head = GLNode(ElemTag.Head)
        cur = head

        while chs:
            ch = chs[0]
            if ch == "(":
                cur.next = GLNode(ElemTag.List)
                cur = cur.next
                cur.subLink = self.parse_content_to_list(chs)
            else:
                chs.pop(0)
                if ch.isdigit() or ch.isalpha():
                    cur.next = GLNode(ElemTag.Atom, ch)
                    cur = cur.next
                elif ch == ")":
                    break

        return head

    def __str__(self) -> str:
        return self.print_list(self.head)

    def print_list(self, node: GLNode) -> str:
        if not node:
            return ""

        content = ""

        cur = node
        while cur:
            if cur.type == ElemTag.Head:
                content += "("
            elif cur.type == ElemTag.Atom:
                content += cur.value
                if cur.next:
                    content += ","
            elif cur.type == ElemTag.List:
                content += self.print_list(cur.subLink)
                if cur.next:
                    content += ","
            cur = cur.next

        content += ")"

        return content
