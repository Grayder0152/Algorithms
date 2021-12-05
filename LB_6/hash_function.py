import math
from abc import ABCMeta, abstractmethod
from typing import Union


class BaseHashFunction(metaclass=ABCMeta):
    def __init__(self, key: Union[int, float, str], size: int):
        self._key = key
        self._size = size

    @abstractmethod
    def hash(self) -> int:
        pass


class HashDivisionMethod(BaseHashFunction):
    """Hash function by division method."""

    def hash(self, ) -> int:
        return self._key % self._size


class HashMultiplicationMethod(BaseHashFunction):
    """Hash function by multiplication method."""

    def hash(self) -> int:
        a = 0.6180339887
        hsh = int(self._size * math.modf(a * self._key)[0])
        return hsh


class HashStringKeyMethod(BaseHashFunction):
    """Hash function by the method of string keys."""

    def __init__(self, key_, size_):
        super().__init__(key_, size_)
        self.a = 2

    def _set_a(self):
        while True:
            if math.gcd(self.a, self._size) == 1:
                break
            self.a += 1

    def hash(self) -> int:
        if not isinstance(self._key, str):
            raise ValueError()
        self._set_a()
        sum_ = 0
        for n, b in enumerate(bytearray(self._key.encode())):
            sum_ += b * pow(self.a, n)
        return sum_ % self._size
