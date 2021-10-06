from unittest import TestCase, main
from LB_4.queue_ import MyQueue, Item


class TestMyQueue(TestCase):
    def setUp(self):
        self.queue_ = MyQueue()

        self.queue_.append('1')
        self.queue_.append('2')
        self.queue_.append('3')
        self.queue_.append('4')

        print()
        self.queue_.display()
        print('-----------------------------------------')

    def test_append(self):
        self.assertEqual(self.queue_.last, '4')
        self.queue_.append('5')
        self.assertEqual(self.queue_.last, '5')
        self.queue_.append(Item('6'))
        self.assertEqual(self.queue_.last, '6')

    def test_pop(self):
        self.assertEqual(self.queue_.first, '1')
        self.queue_.pop()
        self.assertEqual(self.queue_.first, '2')

    def test_replace_first_with_last(self):
        self.assertEqual(self.queue_.first, '1')
        self.assertEqual(self.queue_.first.next_item, '2')
        self.assertEqual(self.queue_.last, '4')

        self.queue_.replace_first_with_last()

        self.assertEqual(self.queue_.first, '4')
        self.assertEqual(self.queue_.first.next_item, '2')
        self.assertEqual(self.queue_.last, '1')

    def test_expand(self):
        self.assertEqual(self.queue_.first, '1')
        self.assertEqual(self.queue_.first.next_item, '2')
        self.assertEqual(self.queue_.last, '4')
        self.assertEqual(self.queue_.last.before_item, '3')

        self.queue_.expand()

        self.assertEqual(self.queue_.first, '4')
        self.assertEqual(self.queue_.first.next_item, '3')
        self.assertEqual(self.queue_.last, '1')
        self.assertEqual(self.queue_.last.before_item, '2')

    def test_is_in_stack(self):
        self.assertTrue(self.queue_.is_in_stack('1'))
        self.assertTrue(self.queue_.is_in_stack(Item('1')))

        self.assertFalse(self.queue_.is_in_stack('0'))
        self.assertFalse(self.queue_.is_in_stack(Item('0')))

    def test_clear(self):
        self.assertFalse(self.queue_.is_empty())
        self.queue_.clear()
        self.assertTrue(self.queue_.is_empty())

    def tearDown(self):
        self.queue_.display()


if __name__ == '__main__':
    main()
