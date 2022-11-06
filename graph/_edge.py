from __future__ import annotations

from ._vertex import Vertex


class Edge:
    def __init__(
        self,
        from_vertex: Vertex,
        to_vertex: Vertex,
        weight: int = 1,
    ) -> None:
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __eq__(self, other: Edge) -> bool:
        return (
            self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex
        )

    def __hash__(self) -> int:
        return hash((self.from_vertex, self.to_vertex))

    def __repr__(self) -> str:
        return f"Edge({self.from_vertex.key} --{self.weight}-> {self.to_vertex.key})"

    def opposite(self) -> Edge:
        return Edge(self.to_vertex, self.from_vertex, self.weight)
