from abc import ABC
from typing import Optional

from LB_2.nodes import Node


class BaseLinkedList(ABC):
    def __init__(self):
        self.head_val: Optional[Node] = None

    def get_node_by_index(self, node_index: int) -> Node:
        """Method for getting the node of list by index."""

        head = self.head_val
        index = 1

        while head is not None:
            if node_index == index:
                return head
            index += 1
            head = head.next_val
        raise IndexError(f'Index {node_index} out of nodes range')

    def get_before_node_of_node(self, node: Node) -> Optional[Node]:
        """Method for getting the before node of node."""

        if node == self.head_val:
            return None

        head = self.head_val

        while head is not None:
            if head.next_val == node:
                return head
            head = head.next_val

            if head == self.head_val:
                break

        raise ValueError(f'The node "{node.data_val}" not in the list')

    def display_list(self) -> None:
        """Method for display all nodes of list."""

        head = self.head_val

        while head is not None:
            print(head.data_val)

            head = head.next_val
            if head == self.head_val:
                break

    def __len__(self):
        count = 0
        head = self.head_val

        while head is not None:
            count += 1

            head = head.next_val
            if head == self.head_val:
                break
        return count
