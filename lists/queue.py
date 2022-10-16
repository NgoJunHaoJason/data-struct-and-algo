from .singly_linked_list import SinglyLinkedList


class Queue:
    def __init__(self) -> None:
        self.linked_list = SinglyLinkedList()

    def __len__(self) -> int:
        return self.linked_list.length

    def __repr__(self) -> str:
        return f"Queue({', '.join(str(value) for value in self.linked_list)})"

    def enqueue(self, value: int) -> None:
        self.linked_list.insert(self.linked_list.length, value)

    def dequeue(self) -> int:
        return self.linked_list.pop(0)
