from __future__ import annotations


class LinkedList:
    def __init__(self, *values: list[int]) -> None:
        self.head_node = ListNode(values[0], None) if values else None
        self.length = 1 if values else 0

        previous_node = self.head_node

        for value in values[1:]:
            previous_node.next_node = ListNode(value, None)
            previous_node = previous_node.next_node

            self.length += 1

    def __getitem__(self, index: int) -> int:
        if self.head_node is None:
            raise IndexError

        if index == 0:
            return self.head_node.value

        current_node = self.head_node

        for _ in range(index):
            current_node = current_node.next_node

            if current_node is None:
                raise IndexError

        return current_node.value
    
    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)


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
    def __init__(self, value: int, next_node: ListNode) -> None:
        self.value = value
        self.next_node = next_node
