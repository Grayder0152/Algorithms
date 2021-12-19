from typing import Union, Any, Optional

from node import Node


class Tree:
    def __init__(self, root_node: Optional[Node] = None):
        self.root: Optional[Node] = root_node

    def __repr__(self):
        return f"Tree with root node {self.root}"

    def insert_node(self, node: Node) -> Node:
        if self.root is None:
            self.root = node
        else:
            if self.root >= node:
                if self.root.left is None:
                    node.parent = self.root
                    self.root.left = node
                else:
                    self.root.left.add_child(node)
            else:
                if self.root.right is None:
                    node.parent = self.root
                    self.root.right = node
                else:
                    self.root.right.add_child(node)
        return node

    def find_node(self, key: Any):
        if self.root is None:
            return
        if self.root == key:
            return self.root

        if self.root >= key:
            if self.root.left is None:
                return
            return self.root.left.find_child(key)
        else:
            if self.root.right is None:
                return
            return self.root.right.find_child(key)

    def remove_node(self, key: Any):
        node = self.find_node(key)
        if node:
            node_children = [node.left, node.right]
            if not any(node_children):
                if node.parent is not None:
                    if node.is_left():
                        node.parent.left = None
                    else:
                        node.parent.right = None
                    node.parent = None
                else:
                    self.root = None
            elif not all(node_children):
                if node.left is not None:
                    node.left.parent = node.parent
                else:
                    node.right.parent = node.parent
                if node.parent is None:
                    self.root = node.left or node.right
                elif node.is_left():
                    node.parent.left = node.left or node.right
                else:
                    node.parent.right = node.left or node.right

            else:
                count_posterity = node.count_posterity()
                if count_posterity['left'] > count_posterity['right']:
                    new_node = node.left.get_max_child()
                else:
                    new_node = node.right.get_min_child()
                if new_node.is_left():
                    new_node.parent.left = None
                else:
                    new_node.parent.right = None
                new_node.parent = node.parent
                if node.parent is None:
                    self.root = new_node
                elif node.is_left():
                    node.parent.left = new_node
                else:
                    node.parent.right = new_node
                new_node.left = node.left
                new_node.right = node.right
                if new_node.left is not None:
                    new_node.left.parent = new_node
                if new_node.right is not None:
                    new_node.right.parent = new_node

            return True
        return False


def display_tree(node, pos=None):
    if node is None:
        return
    prefix = ""
    sep = f'{" " * node.get_level()}'
    if node.parent:
        prefix = sep + f"{pos}:|__"
        if node.parent.parent is not None:
            prefix = ' ' * 2 + prefix
    print(f"{prefix}{node.key}")
    if node.left:
        display_tree(node.left, pos="LEFT")
    if node.right:
        display_tree(node.right, pos="RIGHT")


if __name__ == '__main__':
    tree = Tree()
    n1 = Node(12, 'Data')
    n2 = Node(42, 'Dfse')
    tree.insert_node(n1)
    tree.insert_node(n2)
    tree.insert_node(Node(2, 'asda1'))
    tree.insert_node(Node(122, 'asda2'))
    tree.insert_node(Node(44, 'asda3'))
    tree.insert_node(Node(4, 'asda4'))

    display_tree(tree.root)
