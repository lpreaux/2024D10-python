import ctypes
from typing import Optional

from exceptions import ArrayError


class Array:
    def __init__(self, size: int = 0, initial_value: Optional[object] = None) -> None:
        self.array_size: int = size
        self.items: ctypes.Array = self._create_array(self.array_size)
        for i in range(self.array_size):
            self.items[i] = initial_value

    @staticmethod
    def _create_array(array_capacity) -> ctypes.Array:
        return (ctypes.py_object * array_capacity)()

    def __len__(self) -> int:
        return self.array_size

    def __getitem__(self, index: int) -> object:
        if index < 0 or index >= self.array_size:
            raise ArrayError("Index out of range")
        return self.items[index]

    def __setitem__(self, index: int, value: object) -> None:
        if index < 0 or index >= self.array_size:
            raise ArrayError("Index out of range")
        self.items[index] = value
