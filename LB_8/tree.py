from node import Node


class Tree:
    def __init__(self, _root_node):
        self.__root_node = _root_node

    def __repr__(self):
        return f"Tree with root node {self.root_node}"

    @property
    def root_node(self):
        return self.__root_node

    def add_node(self, data, parent):
        if self.find_node(data):
            raise AttributeError(f"Node with data {data} already exist.")
        if parent is None:
            raise ValueError('If node is not root, it must have parent.')
        return Node(data, parent)

    def find_node(self, data):
        if self.root_node.data == data:
            return self.root_node
        for ch in self.root_node.children:
            node = ch if ch.data == data else ch.find_children(data)
            if node:
                return node

    def remove_node(self, data):
        node = self.find_node(data)
        if node:
            for ch in node.children:
                ch.remove_children()
            if node.parent:
                node.parent.children.remove(node)
            node.parent = None
            node.children = []
            del node


if __name__ == '__main__':
    root_node = Node('A')
    tree = Tree(root_node)
    n1 = tree.add_node('B', tree.root_node)
    tree.add_node('C', tree.root_node)
    tree.add_node('D', n1)
