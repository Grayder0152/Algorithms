import os

from nodes import Child, Node, TicketNumber
from linked_lists.singly import SinglyLinkedList, generate_singly_linked_list
from linked_lists.circular_singly import CircularSinglyLinkedList


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
    os.system('cls' if os.name == 'nt' else 'clear')

    match list_:
        case '1':
            singly_list()
        case '2':
            print("Not Found")
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
    6 - впорядкувати елементи в списку за зростанням(спаданням);
    7 - створення копії списку;
    8 - очищення списку.
        """
    )
    os.system('cls' if os.name == 'nt' else 'clear')
    linked_list = generate_and_display_list()
    match method:
        case '1':
            node = Node('Node_0')
            linked_list.add_node_to_begin(node)
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            pass
        case _:
            pass
    print("Кінцева версія списка:")
    linked_list.display_list()


if __name__ == '__main__':
    console_dialog_window()
