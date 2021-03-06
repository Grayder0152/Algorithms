from typing import Any


class Item:
    def __init__(self, value):
        self.__value = value
        self.next_item = None
        self.before_item = None

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.value == other.value
        else:
            return self.value == other


class Stack:
    def __init__(self):
        self.last: [None, Item] = None
        self.first: [None, Item] = None

    def __len__(self) -> int:
        """Get length of the stack"""

        head = self.last
        length = 0
        while head is not None:
            length += 1
            head = head.before_item
        return length

    def append(self, value: Any) -> None:
        """Append item to stack"""

        item = Item(value) if not isinstance(value, Item) else value

        if self.last is None:
            self.last = item
            self.first = item
        else:
            if self.last is self.first:
                self.first.next_item = item
            else:
                self.last.next_item = item
            item.before_item = self.last
            self.last = item

    def clear(self) -> None:
        """Clear the stack"""

        while self.last is not None:
            self.pop()

    def display(self) -> None:
        """Print all elements of the stack"""

        if self.is_empty():
            print('Stack is empty!')
        else:
            head = self.last
            while head is not None:
                print(head)
                head = head.before_item

    def is_in_stack(self, value) -> bool:
        """Check if item in the stack"""

        head = self.last

        while head is not None:
            if head == value:
                return True
            head = head.before_item
        return False

    def is_empty(self) -> bool:
        """Check if the stack is empty"""

        return not all([self.first, self.last])

    def expand(self) -> None:
        """Expand the stack"""

        items = []
        while self.last is not None:
            items.append(self.pop())

        for item in items:
            self.append(item)

    def pop(self) -> Item:
        """Delete last item of the stack"""

        if self.last is self.first:
            item = self.last
            self.first = None
            self.last = None
        else:
            self.last.before_item.next_item = None
            item = self.last
            self.last = self.last.before_item
        item.next_item = None
        item.before_item = None
        return item

    def replace_first_with_last(self) -> None:
        """Replace first item with last item of the stack"""

        last = self.last.before_item
        first = self.first.next_item

        self.first.next_item = None
        self.last.before_item = None

        self.first, self.last = self.last, self.first

        first.before_item = self.first
        last.next_item = self.last

        self.first.next_item = first
        self.last.before_item = last
        self.first.before_item = None


if __name__ == '__main__':
    stack = Stack()
    stack.append('1')
    stack.append('2')
    stack.append('3')
    stack.append('4')
    stack.append('5')
    stack.append('6')
    print('-----------------------------------------')
    stack.display()
    stack.pop()
    print(stack.is_in_stack('4'))
    print(stack.is_in_stack('1'))

    stack.replace_first_with_last()
    print('-----------------------------------------')
    stack.display()

    stack.expand()
    print('-----------------------------------------')
    stack.display()

    stack.clear()
    print('-----------------------------------------')
    stack.display()
