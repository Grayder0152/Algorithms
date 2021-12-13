from LB_8.node import Node
from traversal import Traversal
from tree import Tree
from utils import display_tree


if __name__ == '__main__':
    tree = Tree(Node('A'))
    tr = Traversal(tree)
    display_tree(tree.root_node)

    while True:
        print("-" * 50)
        inp = input(
            """
    Оберіть опперацію з деревом('q' - вийти):
        1 - додавання;
        2 - видалення;
        3 - пошук;
        4 - прямий обхід дерева;
        5 - зворотній обхід дерева;
        6 - симетричний обхід дерева.
            """
        )
        match inp:
            case '1':
                data = input("Данні: ")
                parent_data = input("Данні вузла предка: ")
                parent = tree.find_node(parent_data)
                tree.add_node(data, parent)
            case '2':
                data = input("Данні: ")
                tree.remove_node(data)
            case '3':
                data = input("Данні: ")
                node = tree.find_node(data)
                if node is None:
                    print('Not found.')
                    continue
                print(node)
            case '4':
                data = input("Данні: ")
                print(tr.traversal_pre_order_with_find(data))
            case '5':
                data = input("Данні: ")
                print(tr.traversal_in_order_with_find(data))
            case '6':
                data = input("Данні: ")
                print(tr.traversal_post_order_with_find(data))
            case 'q':
                break
            case _:
                print("Номер не вірний!")
        print("-" * 50)
        display_tree(tree.root_node)
