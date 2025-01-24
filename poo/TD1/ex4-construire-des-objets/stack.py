from typing import Optional

from custom_array import Array
from exceptions import StackError


class Stack:
    def __init__(self, max_size: Optional[int] = None) -> None:
        self.max_size: Optional[int] = max_size
        self.item_count: int = 0
        self.stack_capacity: int = self.max_size if self.max_size is not None else 1
        self.items: Array = Array(self.stack_capacity)

    def __len__(self) -> int:
        return self.item_count

    def is_empty(self) -> bool:
        return self.item_count == 0

    def is_full(self) -> bool:
        return self.max_size is not None and self.item_count >= self.max_size

    def push(self, item: object) -> None:
        if self.item_count == self.stack_capacity:
            self._grow_capacity()
        self.items[self.item_count] = item
        self.item_count += 1

    def _grow_capacity(self) -> None:
        if self.is_full():
            raise StackError('Stack is full')

        new_capacity = self.stack_capacity * 2
        self.stack_capacity = min(new_capacity, self.max_size) if self.max_size is not None else new_capacity
        new_array = Array(self.stack_capacity)
        for i in range(self.item_count):
            new_array[i] = self.items[i]

        self.items = new_array

    def peek(self) -> object:
        if self.is_empty():
            raise StackError('Stack is empty')
        return self.items[self.item_count - 1]

    def pop(self) -> object:
        if self.is_empty():
            raise StackError('Stack is empty')
        self.item_count -= 1
        item = self.items[self.item_count]
        self.items[self.item_count] = None
        return item

    def clear(self) -> None:
        for i in range(self.item_count):
            self.pop()

    def reverse(self) -> None:
        new_array = Array(self.stack_capacity)
        for i in range(self.item_count):
            new_array[i] = self.items[self.item_count - 1 - i]
        self.items = new_array

    def afficher(self) -> None:
        if self.is_empty():
            print('Stack is empty')
            return

        print(f"Stack contains {self.item_count} item{'s' if self.item_count > 1 else ''}:")
        for i in range(self.item_count):
            print(f"- {self.items[i]}")
