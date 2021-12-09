from typing import Any, Optional, List

from LB_6.item import Item
from hash_function import HashDivisionMethod


class HashTable:
    __DELETED = 'Deleted'
    __EMPTY = None

    def __init__(self):
        self.__size: int = 2
        self.__table: List[Optional[Item, str]] = [self.__EMPTY] * self.__size
        self.__max_fill_factor: float = 0.7

    @property
    def size(self) -> int:
        return self.__size

    def __getitem__(self, _key: int) -> Any:
        hash_code = self._hash(_key)
        cell = self.__table[hash_code]

        if self.is_free_cell(cell):
            return self.__EMPTY
        elif cell.key == _key:
            return cell

        cycle_list = self.__table[hash_code + 1:] + self.__table[:hash_code]
        for i in cycle_list:
            if i is self.__EMPTY:
                return self.__EMPTY
            elif i == self.__DELETED:
                continue
            elif i.key == _key:
                return i

    def __setitem__(self, _key: int, _value: Any) -> None:
        if self[_key] is not self.__EMPTY:
            raise KeyError("This key already used!")

        item = Item(_key, _value)
        hash_code = self._hash(_key)

        if not isinstance(self.__table[hash_code], Item):
            self.__table[hash_code] = item
        else:
            cycle_list = list(enumerate(self.__table))[hash_code + 1:] + list(enumerate(self.__table))[:hash_code]
            for h, i in cycle_list:
                if self.is_free_cell(i):
                    self.__table[h] = item
                    break
        if self.get_fill_factor() > self.__max_fill_factor:
            self.__rebuild_table()

    def __delitem__(self, _key: int):
        item = self[_key]
        if item is self.__EMPTY:
            raise KeyError("Key not found!")

        hash_code = self._hash(_key)
        if item.key == _key:
            self.__table[hash_code] = self.__DELETED
        else:
            cycle_list = list(enumerate(self.__table))[hash_code + 1:] + list(enumerate(self.__table))[:hash_code]
            for h, i in cycle_list:
                if not self.is_free_cell(i) and i.key == _key:
                    self.__table[h] = self.__DELETED
                    break

    def __str__(self) -> str:
        str_table = []
        for index, item in enumerate(self.__table):
            str_table.append(f"{index} - {item}")
        return '\n'.join(str_table)

    def _hash(self, _key: Any) -> int:
        return HashDivisionMethod(_key, self.size).hash()

    def get_fill_factor(self) -> float:
        free_cells = 0
        for cell in self.__table:
            if not isinstance(cell, Item):
                free_cells += 1
        return (self.__size - free_cells) / self.__size

    @staticmethod
    def is_free_cell(_cell) -> bool:
        return False if isinstance(_cell, Item) else True

    def __rebuild_table(self) -> None:
        old_items = (i for i in self.__table if self.is_free_cell(i))

        self.__size = self.size * 2
        self.__table = [self.__EMPTY] * self.size

        for item in old_items:
            self[item.key] = item.value


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
