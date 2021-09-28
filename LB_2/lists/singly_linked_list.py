class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


def merge_linked_lists(list_1, list_2):
    merged_list = list_1
    head = merged_list.head_val
    while True:
        head = head.next_val
        if head.next_val is None:
            head.next_val = list_2.head_val
            break
    return merged_list


def create_list_with_common_nodes(list_1, list_2):
    common_list = SinglyLinkedList()
    head_1 = list_1.head_val
    head_2 = list_2.head_val
    nodes_1 = set()
    nodes_2 = set()
    while head_1 is not None:
        nodes_1.add(head_1.data_val)
        head_1 = head_1.next_val

    while head_2 is not None:
        nodes_2.add(head_2.data_val)
        head_2 = head_2.next_val

    common_nodes = nodes_1 & nodes_2
    head = list_1.head_val
    index = 0
    while head is not None:
        if head.data_val in common_nodes:
            if index == 0:
                common_list.head_val = Node(head.data_val)
                common_head = Node(head.data_val)
                index = 1
            common_head.next_val = Node(head.data_val)
            common_head = Node(head.data_val)
        head = head.next_val

    common_list.print_list()


if __name__ == '__main__':
    linked_list_1 = SinglyLinkedList()
    linked_list_1.head_val = Node("A")

    n2 = Node("B")
    n3 = Node("C")
    n4 = Node("D")

    linked_list_1.head_val.next_val = n2
    n2.next_val = n3
    n3.next_val = n4
    linked_list_1.print_list()
    print('_____________________________')

    linked_list_2 = SinglyLinkedList()
    linked_list_2.head_val = Node("I")

    n2 = Node("A")
    n3 = Node("G")
    n4 = Node("J")

    linked_list_2.head_val.next_val = n2
    n2.next_val = n3
    n3.next_val = n4
    linked_list_2.print_list()
    print('_____________________________')

    create_list_with_common_nodes(linked_list_1, linked_list_2)
