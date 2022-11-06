from __future__ import annotations
from abc import ABC, abstractmethod

from ._vertex import Vertex


class Edge(ABC):
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: int = 1) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __hash__(self) -> int:
        return hash((self.vertex1, self.vertex2))

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError


class UnidirectionalEdge(Edge):
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: int = 1) -> None:
        super().__init__(vertex1, vertex2, weight)

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, UnidirectionalEdge)
            and self.vertex1 == other.vertex1
            and self.vertex2 == other.vertex2
        )

    def __repr__(self) -> str:
        return f"UnidirectionalEdge({self.vertex1.key} --{self.weight}-> {self.vertex2.key})"

    def opposite(self) -> UnidirectionalEdge:
        return UnidirectionalEdge(self.vertex2, self.vertex1, self.weight)


class BidirectionalEdge(Edge):
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: int = 1) -> None:
        if vertex1.key <= vertex2.key:
            super().__init__(vertex1, vertex2, weight)
        else:
            super().__init__(vertex2, vertex1, weight)

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BidirectionalEdge) and (
            (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2)
            or (self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1)
        )

    def __repr__(self) -> str:
        return f"BidirectionalEdge({self.vertex1.key} --{self.weight}-- {self.vertex2.key})"
