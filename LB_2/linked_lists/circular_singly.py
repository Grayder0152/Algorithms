from LB_2.nodes import Child, TicketNumber
from LB_2.linked_lists.base_linked_list import BaseLinkedList


class CircularSinglyLinkedList(BaseLinkedList):
    def get_before_node_of_node(self, node):
        """Method for getting the before node of node"""

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


def generate_circular_singly_linked_list(n: int, node: [Child, TicketNumber]) -> CircularSinglyLinkedList:
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

    children = generate_circular_singly_linked_list(count, Child)
    tickets = generate_circular_singly_linked_list(count, TicketNumber)

    child_index = 0
    ticket_index = 0

    iteration = 0
    while iteration != count:
        child_index += children_recount
        ticket_index += tickets_recount

        child_node = children.get_node_by_index(child_index)
        ticket_node = tickets.get_node_by_index(ticket_index)

        result[child_node.data_val] = ticket_node.data_val

        children.remove_node_by_index(child_index)
        tickets.remove_node_by_index(ticket_index)

        iteration += 1

    return result
