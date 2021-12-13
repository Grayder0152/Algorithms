from typing import Optional, Any, List


class Node:
    def __init__(self, data: Any, parent: Optional['Node'] = None):
        self.data = data
        self.children: List['Node'] = []
        self.parent = self.set_parent(parent)

    def __repr__(self):
        return f"{self.data}"

    def set_parent(self, parent):
        if parent is not None:
            parent.children.append(self)
        return parent

    def get_level(self):
        depth = 0
        parent = self.parent
        while parent is not None:
            depth += 1
            parent = parent.parent

        return depth

    def find_children(self, data):
        for ch in self.children:
            return ch if ch.data == data else ch.find_children(data)

    def remove_children(self):
        for ch in self.children:
            if ch.children:
                ch.remove_children()
            ch._parent = None
            ch.children = []
            del ch


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B", node1)
