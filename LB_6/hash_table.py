from typing import Any, Optional, List, Union

from LB_6.item import Item
from hash_function import HashDivisionMethod


class HashTable:
    def __init__(self):
        self.__size = 3
        self.__table: List[Optional[Item]] = [None] * self.__size

    @property
    def size(self) -> int:
        return self.__size

    def __getitem__(self, key: Union[int, str]) -> Any:
        hash_code = self._hash(key)
        item = self.__table[hash_code]
        if item is None:
            return None
        elif item.next is None and item.key == key:
            return item.value
        else:
            head = item
            while head is not None:
                if head.key == key:
                    return head.value
                head = head.next

    def __setitem__(self, key: Union[int, str], value: Any) -> None:
        if self[key] is not None:
            raise KeyError("Key already used!")

        item = Item(key, value)
        hash_code = self._hash(key)

        if self.__table[hash_code] is None:
            self.__table[hash_code] = item
        else:
            head = self.__table[hash_code]
            while head.next is not None:
                head = head.next
            head.next = item

    def __delitem__(self, key: Union[int, str]):
        if self[key] is None:
            raise KeyError("Key not found!")

        hash_code = self._hash(key)
        item = self.__table[hash_code]
        if item.next is None:
            del item
            self.__table[hash_code] = None
        else:
            head = item
            before = None
            while head.next is not None and head.key != key:
                before = head
                head = head.next
            if before is None:
                self.__table[hash_code] = head.next
            else:
                before.next = head.next

    def __str__(self) -> str:
        str_table = []
        for index, item in enumerate(self.__table):
            if item is None:
                str_table.append(f"{index} - None")
            elif item.next is None:
                str_table.append(f"{index} - {item}")
            else:
                items = []
                head = item
                while head is not None:
                    items.append(str(head))
                    head = head.next
                str_table.append(f"{index} - {' -> '.join(items)}")
        return '\n'.join(str_table)

    def _hash(self, key: Any) -> int:
        return HashDivisionMethod(key, self.size).hash()


if __name__ == '__main__':
    hash_table = HashTable()
    print(hash_table)

    while True:
        print("-" * 50)
        inp = input(
            """
    Оберіть опперацію з хеш-таблицею('q' - вийти):
        1 - додавання нової пари «ключ-значення»;
        2 - видалення пари «ключ-значення» за ключем;
        3 - пошук значення за ключем.
            """
        )
        match inp:
            case '1':
                key = int(input("Ключ: "))
                value = int(input("Значення: "))
                hash_table[key] = value
            case '2':
                key = int(input("Ключ: "))
                del hash_table[key]
            case '3':
                key = int(input("Ключ: "))
                print(f'value = {hash_table[key]}')
            case 'q':
                break
            case _:
                print("Номер не вірний!")
        print("-" * 50)
        print(hash_table)
