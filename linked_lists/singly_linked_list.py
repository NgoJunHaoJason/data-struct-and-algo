from __future__ import annotations
from typing import Union


class SinglyLinkedList:
    def __init__(self, *values: list[int]) -> None:
        self.sentinel_node = SinglyLinkedListNode(None)
        self.length = len(values)

        previous_node = self.sentinel_node

        for value in values:
            previous_node.next_node = SinglyLinkedListNode(value)
            previous_node = previous_node.next_node

    def __getitem__(self, subscript: Union[int, slice]) -> Union[int, SinglyLinkedList]:

        if isinstance(subscript, int):
            return self._get_value(subscript)
        elif isinstance(subscript, slice):
            return self._get_slice(subscript)
        else:
            raise TypeError

    def _get_value(self, subscript: int) -> int:
        if self.sentinel_node.next_node is None:
            raise IndexError

        index = self._make_index_positive(subscript)

        if index >= self.length:
            raise IndexError

        current_node = self.sentinel_node.next_node

        for _ in range(index):
            current_node = current_node.next_node

        return current_node.value

    def _get_slice(self, subscript: slice) -> SinglyLinkedList:
        start, stop, step = subscript.start, subscript.stop, subscript.step

        start = 0 if start is None else self._make_index_positive(start)
        stop = self.length if stop is None else self._make_index_positive(stop)
        step = 1 if step is None else step

        if step == 0:
            raise ValueError

        if (step > 0 and (start >= self.length or stop <= start)) or (
            step < 0 and (stop >= self.length or start <= stop)
        ):
            return SinglyLinkedList()

        sublist_length = stop - start if step > 0 else start - stop

        existing_node = self.sentinel_node.next_node
        new_linked_list = SinglyLinkedList()

        if step > 0:
            for _ in range(start):
                existing_node = existing_node.next_node

            new_node = SinglyLinkedListNode(existing_node.value)
            first_node = new_node
            for _ in range(sublist_length - 1):
                existing_node = existing_node.next_node
                new_node.next_node = SinglyLinkedListNode(existing_node.value)
                new_node = new_node.next_node

        else:
            for _ in range(stop + 1):
                existing_node = existing_node.next_node

            new_node = None
            for _ in range(0, sublist_length):
                new_node = SinglyLinkedListNode(existing_node.value, new_node)
                existing_node = existing_node.next_node
            first_node = new_node

        new_linked_list.sentinel_node.next_node = first_node
        new_linked_list.length = sublist_length

        return new_linked_list

    def _make_index_positive(self, index: int) -> int:
        return self.length + index if index < 0 else index

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> SinglyLinkedListIterator:
        return SinglyLinkedListIterator(self)

    def __add__(self, other: SinglyLinkedList) -> SinglyLinkedList:
        new_linked_list = self.clone()
        second_half = other.clone()

        if new_linked_list.sentinel_node.next_node is None:
            new_linked_list = second_half
        else:
            last_node = new_linked_list.sentinel_node.next_node
            while last_node.next_node is not None:
                last_node = last_node.next_node

            last_node.next_node = second_half.sentinel_node.next_node

            new_linked_list.length += second_half.length

        return new_linked_list

    def __repr__(self) -> str:
        string_representation = "LinkedList("

        if self.sentinel_node.next_node is None:
            return string_representation + ")"

        current_node = self.sentinel_node.next_node
        while current_node.next_node is not None:
            string_representation += f"{current_node.value}, "
            current_node = current_node.next_node

        string_representation += f"{current_node.value})"
        return string_representation

    def clone(self) -> SinglyLinkedList:
        new_linked_list = SinglyLinkedList()

        new_node = new_linked_list.sentinel_node

        existing_node = self.sentinel_node.next_node
        while existing_node is not None:
            new_node.next_node = SinglyLinkedListNode(existing_node.value)
            new_node = new_node.next_node

            existing_node = existing_node.next_node

        new_linked_list.length = self.length
        return new_linked_list

    def insert(self, index: int, value: int) -> None:
        index = self._make_index_positive(index)

        if index > self.length:
            raise IndexError
        else:
            previous_node = self.sentinel_node

            for _ in range(index):
                previous_node = previous_node.next_node

            new_node = SinglyLinkedListNode(value, previous_node.next_node)
            previous_node.next_node = new_node

        self.length += 1

    def pop(self, index: int) -> int:
        index = self._make_index_positive(index)

        if index >= self.length:
            raise IndexError
        else:
            previous_node = self.sentinel_node
            for _ in range(index):
                previous_node = previous_node.next_node

            value = previous_node.next_node.value
            previous_node.next_node = previous_node.next_node.next_node

        self.length -= 1
        return value

    def remove(self, value: int) -> None:
        if self.sentinel_node.next_node is None:
            raise ValueError

        previous_node = self.sentinel_node
        current_node = self.sentinel_node.next_node

        while current_node is not None:
            if current_node.value == value:
                previous_node.next_node = current_node.next_node
                self.length -= 1
                return

            previous_node = current_node
            current_node = current_node.next_node

        raise ValueError


class SinglyLinkedListIterator:
    def __init__(self, linked_list: SinglyLinkedList) -> None:
        self._current_node = linked_list.sentinel_node.next_node

    def __iter__(self) -> SinglyLinkedListIterator:
        return self

    def __next__(self) -> int:
        if self._current_node is None:
            raise StopIteration

        current_value = self._current_node.value
        self._current_node = self._current_node.next_node

        return current_value


class SinglyLinkedListNode:
    def __init__(self, value: int, next_node: SinglyLinkedListNode = None) -> None:
        self.value = value
        self.next_node = next_node
