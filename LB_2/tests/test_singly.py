from unittest import TestCase, main

from LB_2.linked_lists.singly import SinglyLinkedList, generate_singly_linked_list
from LB_2.nodes import Node


class SinglyLinkedListTests(TestCase):
    def setUp(self):
        self.linked_list = generate_singly_linked_list(5)

    def test_add_node_to_begin(self):
        node = Node('A')
        self.assertEqual(self.linked_list.head_val.data_val, 'Node_1')
        self.linked_list.add_node_to_begin(node)
        self.assertEqual(self.linked_list.head_val, node)
        self.assertEqual(self.linked_list.head_val.data_val, 'A')

    def test_add_node_after_index(self):
        node_1 = Node('A')
        node_2 = Node('B')
        self.linked_list.head_val = node_1
        self.linked_list.add_node_after_index(node_2, 1)
        self.assertEqual(node_1.next_val, node_2)

    def test_move_node_to_n_position(self):
        node_4 = self.linked_list.get_node_by_index(4)
        self.assertEqual(node_4.data_val, 'Node_4')
        self.linked_list.move_node_to_n_position(1, 3)
        node_4 = self.linked_list.get_node_by_index(4)
        self.assertEqual(node_4.data_val, 'Node_1')

    def test_remove_node_by_index(self):
        assert False

    def test_remove_every_n_node(self):
        assert False

    def test_sorted_list(self):
        assert False

    def test_create_copy_list(self):
        assert False

    def test_delete_list(self):
        assert False


if __name__ == '__main__':
    main()
