from __future__ import annotations


class Vertex:
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
    
    def __eq__(self, other: Vertex) -> bool:
        return other.name == self.name
    
    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"Vertex({self.name}: {self.value})"
