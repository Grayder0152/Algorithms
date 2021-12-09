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
