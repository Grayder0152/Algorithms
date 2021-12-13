from abc import abstractmethod
from math import ceil
from typing import Union

from node import Node
from tree import Tree
from utils import generate_tree, display_tree


class Order:
    def __init__(self, _tree: Tree, find_node_data):
        self.way = []
        self.tree = _tree
        self.find_node_data = find_node_data

    def _recurse_traversal(self, node: Node, is_left_direction: bool):
        """
        Recursive tree traversal.

        ::param: node - tree node.
        ::param: is_left_direction - True (left subtree are visited) / False(right subtree are visited).
        ::return: None.
        """

        n = ceil(len(node.children) / 2)
        children = node.children[:n] if is_left_direction else node.children[n:]

        for ch in children:
            if self.find(ch):
                return True
        return False

    @abstractmethod
    def find(self, node: Node):
        pass


class PreOrder(Order):
    def find(self, node: Node):
        """
        The root of the tree is visited, then all the nodes of the left subtree,
        then the nodes trail the subtrees to the right
        (root-left-right).

        ::param: node - tree`s node.
        ::return: None.
        """

        self.way.append(node.data)
        if node.data == self.find_node_data or self._recurse_traversal(node=node, is_left_direction=True):
            return True
        return self._recurse_traversal(node=node, is_left_direction=False)


class InOrder(Order):
    def find(self, node: Node):
        """
        First, all the nodes of the left subtree, then sequentially the nodes of
        the remaining subtrees in reverse order, the root is visited last
        (left-root-right).

        ::param: node - tree`s node.
        ::return: None.
        """

        if self._recurse_traversal(node=node, is_left_direction=True):
            return True
        self.way.append(node.data)
        if node.data == self.find_node_data:
            return True
        return self._recurse_traversal(node=node, is_left_direction=False)


class PostOrder(Order):
    def find(self, node: Node):
        """
        All nodes of the left subtree are visited, then the root,
        then sequentially in a symmetric order all the nodes of the remaining subtrees
        (left-right-root).

        ::param: node - tree`s node.
        ::return: None.
        """

        if self._recurse_traversal(node=node, is_left_direction=True):
            return True
        if self._recurse_traversal(node=node, is_left_direction=False):
            return True
        self.way.append(node.data)
        if node.data == self.find_node_data:
            return True
        return False


class Traversal:
    __AVAILABLE_ORDERS = {PostOrder, InOrder, PreOrder}

    def __init__(self, _tree: Tree):
        self.__tree: Tree = _tree
        self.__order: Union[callable(Order), None] = None

    @property
    def tree(self) -> Tree:
        return self.__tree

    def __check_order(self) -> None:
        if self.__order not in self.__AVAILABLE_ORDERS:
            raise ValueError("Order not found.")

    def __traversal_with_find(self, find_node_data: str) -> str:
        self.__check_order()
        traversal = self.__order(self.__tree, find_node_data)
        if traversal.find(self.__tree.root_node):
            return '-->'.join(traversal.way)
        return 'Not Found'

    def traversal_pre_order_with_find(self, find_node_data: str) -> str:
        self.__order = PreOrder
        return self.__traversal_with_find(find_node_data)

    def traversal_in_order_with_find(self, find_node_data: str) -> str:
        self.__order = InOrder
        return self.__traversal_with_find(find_node_data)

    def traversal_post_order_with_find(self, find_node_data: str) -> str:
        self.__order = PostOrder
        return self.__traversal_with_find(find_node_data)


if __name__ == '__main__':
    tree = generate_tree()
    display_tree(tree.root_node)
    t = Traversal(tree)
    print(t.traversal_pre_order_with_find('A'))
    print(t.traversal_in_order_with_find('A'))
    print(t.traversal_post_order_with_find('A'))
