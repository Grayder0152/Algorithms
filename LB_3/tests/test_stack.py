from unittest import TestCase, main
from LB_3.stack import Stack, Item


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

        self.stack.append('1')
        self.stack.append('2')
        self.stack.append('3')
        self.stack.append('4')

        print()
        self.stack.display()
        print('-----------------------------------------')

    def test_append(self):
        self.assertEqual(self.stack.last, '4')
        self.stack.append('5')
        self.assertEqual(self.stack.last, '5')
        self.stack.append(Item('6'))
        self.assertEqual(self.stack.last, '6')

    def test_pop(self):
        self.assertEqual(self.stack.last, '4')
        self.stack.pop()
        self.assertEqual(self.stack.last, '3')

    def test_replace_first_with_last(self):
        self.assertEqual(self.stack.first, '1')
        self.assertEqual(self.stack.first.next_item, '2')
        self.assertEqual(self.stack.last, '4')

        self.stack.replace_first_with_last()

        self.assertEqual(self.stack.first, '4')
        self.assertEqual(self.stack.first.next_item, '2')
        self.assertEqual(self.stack.last, '1')

    def test_expand(self):
        self.assertEqual(self.stack.first, '1')
        self.assertEqual(self.stack.first.next_item, '2')
        self.assertEqual(self.stack.last, '4')
        self.assertEqual(self.stack.last.before_item, '3')

        self.stack.expand()

        self.assertEqual(self.stack.first, '4')
        self.assertEqual(self.stack.first.next_item, '3')
        self.assertEqual(self.stack.last, '1')
        self.assertEqual(self.stack.last.before_item, '2')

    def test_is_in_stack(self):
        self.assertTrue(self.stack.is_in_stack('1'))
        self.assertTrue(self.stack.is_in_stack(Item('1')))

        self.assertFalse(self.stack.is_in_stack('0'))
        self.assertFalse(self.stack.is_in_stack(Item('0')))

    def test_clear(self):
        self.assertFalse(self.stack.is_empty())
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

    def tearDown(self):
        self.stack.display()


if __name__ == '__main__':
    main()
