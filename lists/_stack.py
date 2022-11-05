from ._singly_linked_list import SinglyLinkedList


class Stack:
    def __init__(self) -> None:
        self.linked_list = SinglyLinkedList()

    def __len__(self) -> int:
        return self.linked_list.length

    def __repr__(self) -> str:
        return f"Stack({', '.join(key for key in self.linked_list)})"

    def push(self, key: str) -> None:
        self.linked_list.insert(self.linked_list.length, key)

    def pop(self) -> str:
        return self.linked_list.pop()
