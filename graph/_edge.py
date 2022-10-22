from __future__ import annotations

from ._vertex import Vertex


class UnidirectionalEdge:
    def __init__(
        self,
        from_vertex: Vertex,
        to_vertex: Vertex,
        weight: int = 1,
    ) -> None:
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __eq__(self, other: UnidirectionalEdge) -> bool:
        return (
            self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex
        )

    def __hash__(self) -> int:
        return hash((self.from_vertex, self.to_vertex))

    def __repr__(self) -> str:
        return f"Edge({self.from_vertex.name} --{self.weight}-> {self.to_vertex.name})"


class BidirectionalEdge:
    def __init__(
        self,
        vertex1: Vertex,
        vertex2: Vertex,
        weight: int = 1,
    ) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __eq__(self, other: BidirectionalEdge) -> bool:
        return (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2) or (
            self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1
        )

    def __repr__(self) -> str:
        return f"Edge({self.vertex1.name} --{self.weight}-- {self.vertex2.name})"
