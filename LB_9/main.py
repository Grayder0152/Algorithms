from LB_9.node import Node
from binary_tree import Tree, display_tree

if __name__ == '__main__':
    tree = Tree()
    display_tree(tree.root)

    while True:
        print("-" * 50)
        inp = input(
            """
    Оберіть опперацію з деревом('q' - вийти):
        1 - додавання;
        2 - видалення;
        3 - пошук;
            """
        )
        match inp:
            case '1':
                key = int(input("Key: "))
                data = input("Data: ")
                node = Node(key, data)
                tree.insert_node(node)
            case '2':
                key = int(input("Key: "))
                tree.remove_node(key)
            case '3':
                key = int(input("Key: "))
                node = tree.find_node(key)
                if node is None:
                    print('Not Found')
                    continue
                print(f'Node: {node}')
            case 'q':
                break
            case _:
                print("Номер не вірний!")
        print("-" * 50)
        display_tree(tree.root)
