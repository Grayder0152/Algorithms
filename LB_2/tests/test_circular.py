from unittest import TestCase, main

from LB_2.linked_lists.circular_singly import generate_children_ticket_numbers


class CircularSinglyLinkedListTests(TestCase):
    def test_generate_children_ticket_numbers(self):
        print()

        result = generate_children_ticket_numbers(5, 2, 2)
        self.assertEqual(result['Child_2'], '2')
        self.assertEqual(result['Child_4'], '4')
        self.assertEqual(result['Child_5'], '5')
        self.assertEqual(len(result), 5)
        print(result)

        result = generate_children_ticket_numbers(10, 5, 2)
        self.assertEqual(result['Child_5'], '2')
        self.assertEqual(result['Child_10'], '4')
        self.assertEqual(result['Child_6'], '6')
        self.assertEqual(len(result), 10)
        print(result)


if __name__ == '__main__':
    main()
