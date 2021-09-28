from unittest import TestCase, main

from LB_2.linked_lists.singly import (
    SinglyLinkedList,
    generate_singly_linked_list,
    merge_singly_linked_lists,
    create_list_with_common_nodes
)
from LB_2.nodes import Node


class SinglyLinkedListTests(TestCase):
    def setUp(self):
        self.linked_list = generate_singly_linked_list(5)
        print()

    def test_add_node_to_begin(self):
        self.linked_list.display_list()

        self.assertEqual(self.linked_list.head_val.data_val, 'Node_1')

        node = Node('Node_0')
        self.linked_list.add_node_to_begin(node)

        self.assertEqual(self.linked_list.head_val, node)
        self.assertEqual(self.linked_list.head_val.data_val, 'Node_0')

        print('-----------------------')
        self.linked_list.display_list()

    def test_add_node_after_index(self):
        self.linked_list.display_list()

        node_2_3 = Node('Node_2_3')
        node_6 = Node('Node_6')

        self.linked_list.add_node_after_index(node_6, 5)
        self.linked_list.add_node_after_index(node_2_3, 2)

        self.assertEqual(self.linked_list.get_node_by_index(7), node_6)
        self.assertEqual(self.linked_list.get_node_by_index(3), node_2_3)

        print('-----------------------')
        self.linked_list.display_list()

    def test_move_node_to_n_position(self):
        self.linked_list.display_list()

        node_4 = self.linked_list.get_node_by_index(4)
        self.assertEqual(node_4.data_val, 'Node_4')

        self.linked_list.move_node_to_n_position(1, 3)

        node_4 = self.linked_list.get_node_by_index(4)
        self.assertEqual(node_4.data_val, 'Node_1')

        print('-----------------------')
        self.linked_list.display_list()

    def test_remove_node_by_index(self):
        self.linked_list.display_list()

        node_3 = self.linked_list.get_node_by_index(3)
        self.assertEqual(node_3.data_val, 'Node_3')

        self.linked_list.remove_node_by_index(3)

        node_3 = self.linked_list.get_node_by_index(3)
        self.assertEqual(node_3.data_val, 'Node_4')

        print('-----------------------')
        self.linked_list.display_list()

    def test_remove_every_n_node(self):
        self.linked_list.display_list()

        node_2 = self.linked_list.get_node_by_index(2)
        node_3 = self.linked_list.get_node_by_index(3)

        self.assertEqual(node_2.data_val, 'Node_2')
        self.assertEqual(node_3.data_val, 'Node_3')

        self.linked_list.remove_every_n_node(2)

        node_2 = self.linked_list.get_node_by_index(2)
        node_3 = self.linked_list.get_node_by_index(3)

        self.assertEqual(node_2.data_val, 'Node_3')
        self.assertEqual(node_3.data_val, 'Node_5')

        print('-----------------------')
        self.linked_list.display_list()

    def test_sorted_list(self):
        lkl = SinglyLinkedList()
        node_1 = Node('B')
        node_2 = Node('C')
        node_3 = Node('A')
        node_4 = Node('D')

        lkl.head_val = node_1
        node_1.next_val = node_2
        node_2.next_val = node_3
        node_3.next_val = node_4

        lkl.display_list()

        lkl.sorted_list()

        print('-------------------')
        lkl.display_list()

        self.assertEqual(lkl.get_node_by_index(1).data_val, 'A')
        self.assertEqual(lkl.get_node_by_index(2).data_val, 'B')
        self.assertEqual(lkl.get_node_by_index(3).data_val, 'C')
        self.assertEqual(lkl.get_node_by_index(4).data_val, 'D')

    def test_create_copy_list(self):
        copy_linked_list = self.linked_list.create_copy_list()

        self.assertEqual(self.linked_list.get_node_by_index(1).data_val, copy_linked_list.get_node_by_index(1).data_val)
        self.assertEqual(self.linked_list.get_node_by_index(2).data_val, copy_linked_list.get_node_by_index(2).data_val)
        self.assertEqual(self.linked_list.get_node_by_index(3).data_val, copy_linked_list.get_node_by_index(3).data_val)
        self.assertEqual(self.linked_list.get_node_by_index(4).data_val, copy_linked_list.get_node_by_index(4).data_val)

        self.assertNotEqual(copy_linked_list.get_node_by_index(1), self.linked_list.get_node_by_index(1))
        self.assertNotEqual(copy_linked_list.get_node_by_index(2), self.linked_list.get_node_by_index(2))
        self.assertNotEqual(copy_linked_list.get_node_by_index(3), self.linked_list.get_node_by_index(3))
        self.assertNotEqual(copy_linked_list.get_node_by_index(4), self.linked_list.get_node_by_index(4))

        self.assertNotEqual(copy_linked_list, self.linked_list)

    def test_delete_list(self):
        self.linked_list.delete_list()
        self.assertIsNone(self.linked_list.head_val)

    def test_merge_singly_linked_lists(self):
        copy_linked_list = self.linked_list.create_copy_list()

        merged_list = merge_singly_linked_lists(self.linked_list, copy_linked_list)
        self.assertEqual(merged_list.get_node_by_index(6), copy_linked_list.head_val)

        merged_list.display_list()

    def test_create_list_with_common_nodes(self):
        copy_linked_list = self.linked_list.create_copy_list()
        copy_linked_list.remove_every_n_node(2)
        copy_linked_list.remove_node_by_index(1)

        self.linked_list.display_list()
        print('----------------------')
        copy_linked_list.display_list()

        common_list = create_list_with_common_nodes(self.linked_list, copy_linked_list)

        self.assertEqual(common_list.get_node_by_index(1).data_val, 'Node_3')
        self.assertEqual(common_list.get_node_by_index(2).data_val, 'Node_5')

        print('----------------------')
        common_list.display_list()


if __name__ == '__main__':
    main()
