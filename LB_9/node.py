from typing import Optional, Any


class Node:
    def __init__(self, key: Any, data: Any):
        self.key: Any = key
        self.__data: Any = data
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __setattr__(self, key, value):
        if key in {'parent', 'left', 'right'}:
            if not isinstance(value, (Node, type(None))):
                raise ValueError()
        super().__setattr__(key, value)

    def __repr__(self):
        return f"{self.key}"

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right
        if self.parent:
            if self.parent.left == self:
                self.parent.left = None
            elif self.parent.right == self:
                self.parent.right = None

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return self.key >= other.key
        return self.key >= other

    @property
    def data(self):
        return self.__data

    def get_level(self):
        depth = 0
        parent = self.parent
        while parent is not None:
            depth += 1
            parent = parent.parent

        return depth

    def add_child(self, node: 'Node') -> None:
        if self >= node:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.add_child(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.add_child(node)

    def find_child(self, key: Any):
        if self == key:
            return self
        if self >= key:
            if self.left is None:
                return
            return self.left.find_child(key)
        else:
            if self.right is None:
                return
            return self.right.find_child(key)


if __name__ == '__main__':
    n = Node(45, '45')
    n.add_child(Node(35, '35'))
