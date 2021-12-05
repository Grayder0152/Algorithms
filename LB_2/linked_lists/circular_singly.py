from typing import Union

from LB_2.nodes import Child, TicketNumber
from LB_2.linked_lists.base_linked_list import BaseLinkedList


class CircularSinglyLinkedList(BaseLinkedList):
    def get_before_node_of_node(self, node):
        """Method for getting the before node of node."""

        head = self.head_val

        while True:
            if head.next_val == node:
                return head
            head = head.next_val

            if head == self.head_val:
                break

    def remove_node_by_index(self, node_index):
        """Method for removing the node by index"""

        node = self.get_node_by_index(node_index)
        before_node = self.get_before_node_of_node(node)

        if node == self.head_val:
            self.head_val = node.next_val
            before_node.next_val = self.head_val
        else:
            before_node.next_val = node.next_val


def generate_circular_singly_linked_list(n: int, node: Union[Child, TicketNumber]) -> CircularSinglyLinkedList:
    """Method for generate circular singly linked list"""

    circular_singly_linked_lis = CircularSinglyLinkedList()

    circular_singly_linked_lis.head_val = TicketNumber('1') if node is TicketNumber else Child('Child_1')
    head = circular_singly_linked_lis.head_val

    for number in range(2, n + 1):
        head.next_val = TicketNumber(str(number)) if node is TicketNumber else Child(f'Child_{number}')
        head = head.next_val

    head.next_val = circular_singly_linked_lis.head_val

    return circular_singly_linked_lis


def generate_children_ticket_numbers(count: int, children_recount: int, tickets_recount: int) -> dict:
    """Function for generate random tickets for children"""

    result = {}

    children = generate_circular_singly_linked_list(count, Child).to_list()
    tickets = generate_circular_singly_linked_list(count, TicketNumber).to_list()

    child_index = 0
    ticket_index = 0

    def _get_index(old_index: int, recount: int, list_len):
        index = old_index + recount - 1
        while index > list_len - 1:
            index -= list_len
        return index

    iteration = 0
    while iteration != count:
        child_index = _get_index(child_index, children_recount, len(children))
        ticket_index = _get_index(ticket_index, tickets_recount, len(tickets))

        result[children.pop(child_index)] = tickets.pop(ticket_index)

        iteration += 1
    return result
