from typing import Any, Union


class Item:
    __slots__ = ('__key', '__value')

    def __init__(self, key: Union[str, int], value: Any):
        self.__key: Union[str, int] = key
        self.__value: Any = value

    def __getattr__(self, attr):
        return getattr(self, f"_{self.__class__.__name__}__{attr}")

    def __str__(self):
        return f"({self.key}, {self.value})"

    def __eq__(self, other):
        return self.value == other.value if isinstance(other, Item) else other
