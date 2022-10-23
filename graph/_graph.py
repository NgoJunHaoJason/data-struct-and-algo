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
        return f"Edge({self.from_vertex.name} -{self.weight}-> {self.to_vertex.name})"

    def opposite(self) -> Edge:
        return Edge(self.to_vertex, self.from_vertex, self.weight)


class DirectedGraph:
    def __init__(self, vertices: set[Vertex], edges: set[Edge]) -> None:
        self.adjacency_map: dict[Vertex, list[Edge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self.adjacency_map[edge.from_vertex].append(edge)


class UndirectedGraph:
    def __init__(self, vertices: set[Vertex], edges: set[Edge]) -> None:
        self.adjacency_map: dict[Vertex, list[Edge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self.adjacency_map[edge.from_vertex].append(edge)
            self.adjacency_map[edge.to_vertex].append(edge.opposite())
