from ._edge import BidirectionalEdge
from ._vertex import Vertex


class UndirectedGraph:
    def __init__(self, vertices: set[Vertex], edges: set[BidirectionalEdge]) -> None:
        self.adjacency_map: dict[Vertex, list[BidirectionalEdge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self.adjacency_map[edge.vertex1].append(edge)
            self.adjacency_map[edge.vertex2].append(edge)
