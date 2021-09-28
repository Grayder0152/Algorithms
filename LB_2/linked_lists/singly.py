from LB_2.nodes import Node
from base_linked_list import BaseLinkedList


class SinglyLinkedList(BaseLinkedList):

    def add_node_to_begin(self, new_node: Node) -> None:
        """Method for adding the node to begin of list"""

        new_node.next_val = self.head_val
        self.head_val = new_node

    def add_node_after_index(self, new_node: Node, index: int) -> None:
        """Method for adding the node after node with any index of list"""

        node = self.get_node_by_index(index)
        new_node.next_val = node.next_val
        node.next_val = new_node

    def move_node_to_n_position(self, node_index: int, n: int):
        """Method for moving the node to n positions"""

        node = self.get_node_by_index(node_index)
        before_node = self.get_before_node_of_node(node)

        for _ in range(n):
            next_node = node.next_val

            if next_node is None:
                raise IndexError('The node index out of node range')

            node.next_val = next_node.next_val
            next_node.next_val = node

            if before_node is None:
                self.head_val = next_node
                before_node = next_node
                continue

            before_node.next_val = next_node
            node = next_node.next_val
            before_node = next_node

    def remove_node_by_index(self, node_index: int) -> None:
        """Method for removing the node by index"""

        node = self.get_node_by_index(node_index)
        before_node = self.get_before_node_of_node(node)
        if before_node is None:
            self.head_val = node.next_val
        else:
            before_node.next_val = node.next_val

    def remove_every_n_node(self, node_index: int) -> None:
        """Method for remove each n node in the list"""

        head = self.head_val

        before = None
        index = 1
        while head is not None:
            if index % node_index == 0:
                if before is None or node_index == 1:
                    self.head_val = head.next_val
                else:
                    before.next_val = head.next_val
            index += 1
            before = head
            head = head.next_val

    def sorted_list(self) -> None:
        """Method for sorted the list"""

        head = self.head_val
        current_node = head
        while current_node.next_val is not None:
            if current_node.next_val.data_val > current_node.data_val:
                current_node = current_node.next_val
            else:
                next_node = current_node.next_val
                current_node.next_val = next_node.next_val
                if head.data_val > next_node.data_val:
                    next_node.next_val = head
                    self.head_val = next_node
                    head = self.head_val
                else:
                    before_node = head
                    while next_node.data_val > before_node.next_val.data_val:
                        before_node = before_node.next_val
                    next_node.next_val = before_node.next_val
                    before_node.next_val = next_node

    def create_copy_list(self):
        """Method for create copy of the list"""

        new_linked_list = SinglyLinkedList()
        head = self.head_val
        index = 1
        while head is not None:
            new_node = Node(head.data_val)
            if index == 1:
                new_linked_list.head_val = new_node
            else:
                new_head.next_val = new_node

            new_head = new_node
            head = head.next_val
            index += 1
        return new_linked_list

    def delete_list(self) -> None:
        """Method for delete all list"""

        head = self.head_val
        while head is not None:
            next_node = head.next_val
            head.next_val = None
            head = next_node
        self.head_val = None


def merge_singly_linked_lists(list_1: SinglyLinkedList, list_2: SinglyLinkedList) -> SinglyLinkedList:
    """Function for merging two singly linked lists"""

    merged_list = list_1
    head = merged_list.head_val
    while True:
        head = head.next_val
        if head.next_val is None:
            head.next_val = list_2.head_val
            break
    return merged_list


def create_list_with_common_nodes(list_1: SinglyLinkedList, list_2: SinglyLinkedList) -> SinglyLinkedList:
    """Function for creation singly linked list with common nodes lis_1 and list_2"""

    common_list = SinglyLinkedList()

    head_1 = list_1.head_val
    head_2 = list_2.head_val

    nodes = set()
    while head_1 is not None:
        nodes.add(head_1.data_val)
        head_1 = head_1.next_val

    first_iter = True
    while head_2 is not None:
        if head_2.data_val in nodes:
            if first_iter:
                common_list.head_val = Node(head_2.data_val)
                common_head = common_list.head_val
                head_2 = head_2.next_val
                first_iter = False
                continue
            common_head.next_val = Node(head_2.data_val)
            common_head = common_head.next_val
        head_2 = head_2.next_val

    return common_list


if __name__ == '__main__':
    l1 = SinglyLinkedList()
    n3 = Node('C')
    n4 = Node('A')
    l1.head_val = n3
    l1.add_node_to_begin(n4)

    l2 = SinglyLinkedList()
    n1 = Node('A')
    n2 = Node('C')
    l2.head_val = n1
    n1.next_val = n2
    print('-----------------------')
    c = create_list_with_common_nodes(l1, l2)
    c.display_list()
