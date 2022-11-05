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

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> SinglyLinkedListIterator:
        return SinglyLinkedListIterator(self)

    def __repr__(self) -> str:
        keys_string = ", ".join([key for key in self])
        return f"SinglyLinkedList({keys_string})"

    def _make_index_positive(self, index: int) -> int:
        return self.length + index if index < 0 else index

    def insert(self, index: int, key: str) -> None:
        """Insert a key in this linked list, at the given index

        Analysis
        --------
        - worst case: index is length of this linked list, n
        - time complexity: O(n)
        - additional data structures used: None
        - space complexity: O(1)

        Parameters
        ----------
        index : int
            the position in which to insert the given key
        key : str
            the key to be inserted

        Raises
        ------
        IndexError
            when given index is out of bounds
        """
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
        """Pop a key in this linked list, from the given index

        Analysis
        --------
        - worst case: index is length of this linked list, n
        - time complexity: O(n)
        - additional data structures used: None
        - space complexity: O(1)

        Parameters
        ----------
        index : int, optional
            the position from which to pop a key, by default -1

        Raises
        ------
        IndexError
            when given index is out of bounds
        """
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
        """Remove the given key in this linked list

        Analysis
        --------
        - worst case: key is in last node of this linked list
        - time complexity: O(n)
        - additional data structures used: None
        - space complexity: O(1)

        Parameters
        ----------
        key: str
            the key to be removed from this linked list

        Raises
        ------
        ValueError
            when the key cannot be found within this linked list
        """
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
