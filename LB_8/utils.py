from node import Node
from tree import Tree


def display_tree(node):
    sep = f'{" " * node.get_level()}'
    prefix = ""
    if node.parent:
        prefix = sep + "|__"
        if node.parent.parent is not None:
            prefix = ' ' * 2 + prefix
    print(f"{prefix}{node.data}")
    for child in node.children:
        display_tree(child)


def generate_tree():
    tree = Tree(Node('A'))
    n1 = tree.add_node('B', tree.root_node)

    tree.add_node('C', tree.root_node)
    tree.add_node('D', tree.root_node)

    n4 = tree.add_node('F1', n1)

    tree.add_node('F2', n1)
    tree.add_node('F3', n1)

    tree.add_node('G1', n4)
    tree.add_node('G2', n4)
    return tree
