from ._edge import UnidirectionalEdge
from ._vertex import Vertex


class DirectedGraph:
    def __init__(self, vertices: set[Vertex], edges: set[UnidirectionalEdge]) -> None:
        self.adjacency_map: dict[Vertex, list[UnidirectionalEdge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self.adjacency_map[edge.from_vertex].append(edge)
