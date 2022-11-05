from __future__ import annotations


class ListNode:
    def __init__(self, key: int, next_node: ListNode = None) -> None:
        self.key = key
        self.next_node = next_node


class SinglyLinkedListIterator:
    def __init__(self, linked_list: SinglyLinkedList) -> None:
        self._current_node = linked_list.sentinel_node.next_node

    def __iter__(self) -> SinglyLinkedListIterator:
        return self

    def __next__(self) -> int:
        if self._current_node is None:
            raise StopIteration

        current_key = self._current_node.key
        self._current_node = self._current_node.next_node

        return current_key


class SinglyLinkedList:
    def __init__(self, *keys: str) -> None:
        self.sentinel_node = ListNode(None)
        self.length = len(keys)

        previous_node = self.sentinel_node

        for key in keys:
            previous_node.next_node = ListNode(key)
            previous_node = previous_node.next_node

    def __getitem__(self, subscript: int) -> str:
        if not isinstance(subscript, int):
            raise TypeError

        if self.sentinel_node.next_node is None:
            raise IndexError

        index = self._make_index_positive(subscript)

        if index >= self.length:
            raise IndexError

        current_node = self.sentinel_node.next_node

        for _ in range(index):
            current_node = current_node.next_node

        return current_node.key

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
            string_representation += f"{current_node.key}, "
            current_node = current_node.next_node

        string_representation += f"{current_node.key})"
        return string_representation

    def clone(self) -> SinglyLinkedList:
        new_linked_list = SinglyLinkedList()

        new_node = new_linked_list.sentinel_node

        existing_node = self.sentinel_node.next_node
        while existing_node is not None:
            new_node.next_node = ListNode(existing_node.key)
            new_node = new_node.next_node

            existing_node = existing_node.next_node

        new_linked_list.length = self.length
        return new_linked_list

    def insert(self, index: int, key: str) -> None:
        index = self._make_index_positive(index)

        if index > self.length:
            raise IndexError
        else:
            previous_node = self.sentinel_node

            for _ in range(index):
                previous_node = previous_node.next_node

            new_node = ListNode(key, previous_node.next_node)
            previous_node.next_node = new_node

        self.length += 1

    def pop(self, index: int = -1) -> str:
        index = self._make_index_positive(index)

        if index >= self.length:
            raise IndexError

        previous_node = self.sentinel_node
        for _ in range(index):
            previous_node = previous_node.next_node

        key = previous_node.next_node.key
        previous_node.next_node = previous_node.next_node.next_node

        self.length -= 1
        return key

    def remove(self, key: str) -> None:
        if self.sentinel_node.next_node is None:
            raise ValueError

        previous_node = self.sentinel_node
        current_node = self.sentinel_node.next_node

        while current_node is not None:
            if current_node.key == key:
                previous_node.next_node = current_node.next_node
                self.length -= 1
                return

            previous_node = current_node
            current_node = current_node.next_node

        raise ValueError
