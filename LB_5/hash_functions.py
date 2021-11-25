import math
from abc import ABCMeta, abstractmethod
from typing import Any

AVAILABLE_KEY_TYPE = (int, float, tuple, str)


class BaseHashFunction(metaclass=ABCMeta):

    def __init__(self):
        self.type_to_int = {
            'int': lambda integer: integer,
            'float': lambda flt: sum(int(number) * n for n, number in enumerate(str(flt).split('.'), start=1)),
            'str': lambda string_: sum(ord(symbol_) * n for n, symbol_ in enumerate(string_, start=1)),
            'tuple': lambda seq: self._get_value_sum_for_seq(seq)
        }

    def _get_value_sum_for_seq(self, seq: tuple) -> int:
        value_sum = 0
        for val in seq:
            get_val = self.type_to_int.get(type(val).__name__)
            if get_val is not None:
                value_sum += get_val(val)
            else:
                value_sum += self._get_value_sum_for_seq(val)
        return value_sum

    @abstractmethod
    def hash(self, key: Any, size: int):
        pass


class HashDivisionMethod(BaseHashFunction):
    def hash(self, key: Any, size: int) -> int:
        if isinstance(key, AVAILABLE_KEY_TYPE):
            type_name = type(key).__name__
            key = self.type_to_int[type_name](key)
            hsh = key % size
            return hsh

        raise TypeError(f"Unhashable type {type(key)}")


class HashMultiplicationMethod(BaseHashFunction):
    def hash(self, key: Any, size: int) -> int:
        if isinstance(key, AVAILABLE_KEY_TYPE):
            a = 0.6180339887
            type_name = type(key).__name__
            key = self.type_to_int[type_name](key)
            hsh = int(size * math.modf(a * key)[0])
            return hsh
        raise TypeError(f"Unhashable type {type(key)}")


class HashStringKeyMethod(BaseHashFunction):
    def hash(self, key: Any, size: int) -> int:
        if isinstance(key, AVAILABLE_KEY_TYPE):
            pass
        raise TypeError(f"Unhashable type {type(key)}")


if __name__ == '__main__':
    h = HashDivisionMethod()
    print(h.type_to_int['str']("cat"))
    print(h.type_to_int['str']("tac"))
