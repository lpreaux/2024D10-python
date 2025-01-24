from typing import Optional

from custom_array import Array
from exceptions import QueueError


class Queue:
    def __init__(self, max_size: Optional[int] = None) -> None:
        self.max_size: Optional[int] = max_size
        self.queue_start: int = 0
        self.queue_end: int = -1 # Empty queue
        self.capacity: int = self.max_size if self.max_size is not None else 1
        self.items: Array = Array(self.capacity)

    # Après avoir commencé le TD2, je me rends compte que j'aurais pu utiliser une @property ce qui aurait sans doute été plus pratique.
    def _item_count(self) -> int:
        count = self.queue_end - self.queue_start + 1
        return count if count >= 0 else self.capacity - count

    def __len__(self) -> int:
        return self._item_count()

    def is_empty(self) -> bool:
        return self._item_count() == 0

    def is_full(self) -> bool:
        return self.max_size is not None and self._item_count() >= self.max_size

    def enqueue(self, item: object) -> None:
        if self._item_count() == self.capacity:
            self._grow_capacity()

        new_queue_end = self.queue_end + 1
        self.queue_end = new_queue_end if new_queue_end < self.capacity else 0
        self.items[self.queue_end] = item

    def _grow_capacity(self) -> None:
        if self.is_full():
            raise QueueError('Queue is full')

        new_capacity = self.capacity*2
        self.capacity = min(new_capacity, self.max_size) if self.max_size is not None else new_capacity
        new_array = Array(self.capacity)

        for i in range(self._item_count()):
            new_array[i] = self.items[(self.queue_start + i) % self.capacity]

        self.items = new_array
        self.queue_start = 0
        self.queue_end = self._item_count() - 1

    def dequeue(self) -> object:
        if self.is_empty():
            raise QueueError('Queue is empty')

        item = self.items[self.queue_start]
        self.items[self.queue_start] = None
        new_queue_start = self.queue_start + 1
        self.queue_start = new_queue_start if new_queue_start < self.capacity else 0
        return item

    def afficher(self) -> None:
        if self.is_empty():
            print('Queue is empty')
            return

        print(f"Queue contains {self._item_count()} item{'s' if self._item_count() > 1 else ''}:")
        for i in range(self._item_count()):
            print(f"- {self.items[(self.queue_start + i) % self.capacity]}")