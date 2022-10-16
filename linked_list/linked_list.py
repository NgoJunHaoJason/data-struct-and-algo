from __future__ import annotations
from typing import Union


class LinkedList:
    def __init__(self, *values: list[int]) -> None:
        self.head_node = ListNode(values[0], None) if values else None
        self.length = 1 if values else 0

        previous_node = self.head_node

        for value in values[1:]:
            previous_node.next_node = ListNode(value, None)
            previous_node = previous_node.next_node

            self.length += 1

    def __getitem__(self, subscript: Union[int, slice]) -> Union[int, LinkedList]:

        if isinstance(subscript, int):
            return self._get_value(subscript)
        elif isinstance(subscript, slice):
            return self._get_slice(subscript)
        else:
            raise TypeError

    def _get_value(self, subscript: int) -> int:
        if self.head_node is None:
            raise IndexError

        index = self._make_index_positive(subscript)

        if index >= self.length:
            raise IndexError

        current_node = self.head_node

        for _ in range(index):
            current_node = current_node.next_node

        return current_node.value

    def _get_slice(self, subscript: slice) -> LinkedList:
        start, stop, step = subscript.start, subscript.stop, subscript.step

        start = self._make_index_positive(start)
        stop = self._make_index_positive(stop)
        step = 1 if step is None else step

        if step > 0:
            if start >= self.length:
                return LinkedList()

            current_node = self.head_node

            for _ in range(start):
                current_node = current_node.next_node

            values = []  # TODO: remove intermediate data structure
            sublist_length = stop - start

            for _ in range(0, sublist_length):
                values.append(current_node.value)
                current_node = current_node.next_node

            return LinkedList(*values)

        elif step < 0:
            if stop >= self.length:
                return LinkedList()
            pass
        else:
            raise ValueError

    def _make_index_positive(self, index: int) -> int:
        return self.length + index if index < 0 else index

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)

    def __add__(self, other: LinkedList) -> LinkedList:
        new_linked_list = LinkedList()

        if self.head_node is not None:
            new_linked_list.head_node = ListNode(self.head_node.value)
            new_node = new_linked_list.head_node

            existing_node = self.head_node
            while existing_node.next_node is not None:
                new_node.next_node = ListNode(existing_node.next_node.value)
                new_node = new_node.next_node

                existing_node = existing_node.next_node

            new_linked_list.length += self.length
        
        if other.head_node is not None:
            if new_linked_list.head_node is None:
                new_linked_list.head_node = ListNode(other.head_node.value)
                new_node = new_linked_list.head_node
            else:
                new_node.next_node = ListNode(other.head_node.value)
                new_node = new_node.next_node
            
            existing_node = other.head_node
            while existing_node.next_node is not None:
                new_node.next_node = ListNode(existing_node.next_node.value)
                new_node = new_node.next_node

                existing_node = existing_node.next_node
            
            new_linked_list.length += other.length

        return new_linked_list

    def insert(self, index: int, value: int) -> None:
        index = self._make_index_positive(index)

        if index > self.length:
            raise IndexError
        elif index == 0:
            self.head_node = ListNode(value, self.head_node)
        else:
            previous_node = self.head_node

            for _ in range(index - 1):
                previous_node = previous_node.next_node

            new_node = ListNode(value, previous_node.next_node)
            previous_node.next_node = new_node

        self.length += 1

    def pop(self, index: int) -> int:
        index = self._make_index_positive(index)

        if index >= self.length:
            raise IndexError
        elif index == 0:
            value = self.head_node.value
            self.head_node = self.head_node.next_node
        else:
            previous_node = self.head_node

            for _ in range(index - 1):
                previous_node = previous_node.next_node

            value = previous_node.next_node.value
            previous_node.next_node = previous_node.next_node.next_node

        self.length -= 1
        return value

    def remove(self, value: int) -> None:
        if self.head_node is None:
            raise ValueError

        if self.head_node.value == value:
            self.head_node = self.head_node.next_node
            self.length -= 1
            return

        previous_node = self.head_node
        current_node = self.head_node.next_node

        while current_node is not None:
            if current_node.value == value:
                previous_node.next_node = current_node.next_node
                self.length -= 1
                return

            previous_node = current_node
            current_node = current_node.next_node

        raise ValueError


class LinkedListIterator:
    def __init__(self, linked_list: LinkedList) -> None:
        self._current_node = linked_list.head_node

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> int:
        if self._current_node is None:
            raise StopIteration

        current_value = self._current_node.value
        self._current_node = self._current_node.next_node

        return current_value


class ListNode:
    def __init__(self, value: int, next_node: ListNode = None) -> None:
        self.value = value
        self.next_node = next_node
