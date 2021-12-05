import os

from nodes import Child, Node, TicketNumber
from linked_lists.singly import SinglyLinkedList, generate_singly_linked_list, merge_singly_linked_lists, \
    create_list_with_common_nodes
from linked_lists.circular_singly import CircularSinglyLinkedList, generate_children_ticket_numbers


def generate_and_display_list() -> SinglyLinkedList:
    linked_list = generate_singly_linked_list(5)
    print("Початкова версія списку:")
    linked_list.display_list()
    return linked_list


def console_dialog_window():
    list_ = input(
        """
Виберіть список(номер пунту):
    1 - однозв’язний список;
    2 - кільцевий однозв’язний список;
        """
    )
    print('\n' * 150)

    match list_:
        case '1':
            singly_list()
        case '2':
            circular_list()
        case _:
            print("Code not found")


def singly_list():
    method = input(
        """
Виберіть операцію(номер пункту):
    1 - додавання елементу в початок списку;
    2 - вставлення елементу після n-го елементу списку;
    3 - пересування елемента на n позицій;
    4 - видалення n-го елементу з списку;
    5 - видалення кожного n-го елементу списку;
    6 - впорядкувати елементи в списку за зростанням;
    7 - створення копії списку;
    8 - очищення списку;
    9 - склеювання двох списків;
    10 - створення списку, який містить спільні елементи двох списків.
        """
    )
    print('\n' * 150)
    linked_list = generate_and_display_list()
    match method:
        case '1':
            node_name = input("Введіть назву вузла: ")
            node = Node(node_name)
            linked_list.add_node_to_begin(node)
        case '2':
            node_name = input("Введіть назву вузла: ")
            node = Node(node_name)
            index = input("Введіть індекс після якого хочете додати елемент: ")
            linked_list.add_node_after_index(node, int(index))
        case '3':
            node_index = input("Введіть індекс вузла, який хочете перемістити: ")
            n = input("Введіть к-ть позицій: ")
            linked_list.move_node_to_n_position(int(node_index), int(n))
        case '4':
            node_index = input("Введіть індекс вузла, який хочете видалити: ")
            linked_list.remove_node_by_index(int(node_index))
        case '5':
            n = input("Введіть число: ")
            linked_list.remove_every_n_node(int(n))
        case '6':
            linked_list.sorted_list()
        case '7':
            copy_list = linked_list.create_copy_list()
            print("Копия: ")
            copy_list.display_list()
        case '8':
            linked_list.delete_list()
        case '9':
            copy_linked_list = linked_list.create_copy_list()
            merged_list = merge_singly_linked_lists(linked_list, copy_linked_list)
            print("Склеєний список: ")
            merged_list.display_list()
        case '10':
            copy_linked_list = linked_list.create_copy_list()
            copy_linked_list.remove_every_n_node(2)
            copy_linked_list.remove_node_by_index(1)

            print("Список 1:")
            linked_list.display_list()
            print("Список 2:")
            copy_linked_list.display_list()
            print("Список із спільними елементами:")
            common_list = create_list_with_common_nodes(linked_list, copy_linked_list)
            common_list.display_list()
        case _:
            print("Жодних методів не було виконано!")

    print("Кінцева версія списка:")
    linked_list.display_list()


def circular_list():
    count_ = int(input("Введіть розмір списків: "))
    children_recount = int(input("Введіть число перерахування для учнів: "))
    tickets_recount = int(input("Введіть число перерахування для білетів: "))

    print(generate_children_ticket_numbers(count_, children_recount, tickets_recount))


if __name__ == '__main__':
    circular_list()
