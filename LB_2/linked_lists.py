from .nodes import Node


class SinglyLinkedList:
    def __init__(self):
        self.head_val = None

    def print_list(self):
        head = self.head_val
        while head is not None:
            print(head.data_val)
            head = head.next_val

    def add_node_to_begin(self, new_node: Node):
        new_node.next_val = self.head_val
        self.head_val = new_node

    def add_node_after_index(self, new_node: Node, index: int):
        head = self.head_val
        i = 0
        while head is not None:
            if i == index:
                new_node.next_val = head.next_val
                head.next_val = new_node
                return
            head = head.next_val
            i += 1
        print("Индек не найден")

    def move_node_to_index(self, node_index, count_position):
        head = self.head_val
        index = 0
        while head is not None:
            if node_index == index:
                for i in range(count_position):
                    next = head.next_val
                    head.next_val = next.next_val
                    next.next_val = head

                    if node_index == 0 and i == 0:
                        self.head_val = next
                        before = next
                        continue

                    before.next_val = next
                    head = next.next_val
                    before = next
                break
            before = head
            head = head.next_val
            index += 1

    def remove_node_by_index(self, node_index):
        head = self.head_val

        before = None
        index = 0
        while head is not None:
            if node_index == index:
                if before is None:
                    self.head_val = head.next_val
                else:
                    before.next_val = head.next_val
                break
            index += 1
            before = head
            head = head.next_val

    def remove_every_index_node(self, node_index):
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

    def sorted_list(self):
        head = self.head_val
        current = head
        while current.next_val is not None:
            if current.next_val.data_val > current.data_val:
                current = current.next_val
            else:
                temp = current.next_val
                current.next_val = temp.next_val
                if head.data_val > temp.data_val:
                    temp.next_val = head
                    self.head_val = temp
                    head = self.head_val
                else:
                    inpos = head
                    while temp.data_val > inpos.next_val.data_val:
                        inpos = inpos.next_val
                    temp.next_val = inpos.next_val
                    inpos.next_val = temp

    def create_copy_list(self):
        new_linked_list = SinglyLinkedList()
        head = self.head_val
        index = 0
        while head is not None:
            new_node = Node(head.data_val)
            if index == 0:
                new_linked_list.head_val = new_node
            else:
                new_head.next_val = new_node

            new_head = new_node
            head = head.next_val
            index += 1
        return new_linked_list

    def delete_list(self):
        head = self.head_val
        while head is not None:
            next = head.next_val
            head.next_val = None
            head = next
        self.head_val = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head_val = None

    def print_list(self):
        print_val = self.head_val
        while True:
            print(print_val.data_val)
            print_val = print_val.next_val

            if print_val == self.head_val:
                break

    def remove_node_by_index(self, node_index):
        head = self.head_val

        before = None
        index = 1
        while head is not None:
            if node_index == index:
                if before is None:
                    self.head_val = head.next_val
                else:
                    before.next_val = head.next_val
                break
            index += 1
            before = head
            head = head.next_val

    def get_by_index(self, node_index):
        head = self.head_val

        index = 1
        while True:
            if node_index == index:
                return head
            index += 1
            head = head.next_val
