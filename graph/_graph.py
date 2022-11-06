from __future__ import annotations
from abc import ABC, abstractmethod

from ._edge import Edge
from ._vertex import Vertex


class Graph(ABC):
    @abstractmethod
    def vertices(self) -> list[Vertex]:
        raise NotImplementedError

    @abstractmethod
    def edges(self, from_vertex: Vertex = None) -> list[Edge]:
        raise NotImplementedError


class DirectedGraph(Graph):
    def __init__(self, vertices: set[Vertex], edges: set[Edge]) -> None:
        self._adjacency_map: dict[Vertex, list[Edge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self._adjacency_map[edge.from_vertex].append(edge)

    def vertices(self) -> list[Vertex]:
        return [vertex for vertex in self._adjacency_map.keys()]

    def edges(self, from_vertex: Vertex = None) -> list[Edge]:
        if from_vertex:
            if from_vertex in self._adjacency_map:
                return [edge for edge in self._adjacency_map[from_vertex]]
            else:
                raise ValueError
        else:
            return [edge for edges in self._adjacency_map.values() for edge in edges]


class UndirectedGraph(Graph):
    def __init__(self, vertices: set[Vertex], edges: set[Edge]) -> None:
        self._adjacency_map: dict[Vertex, list[Edge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self._adjacency_map[edge.from_vertex].append(edge)
            self._adjacency_map[edge.to_vertex].append(edge.opposite())

    def vertices(self) -> list[Vertex]:
        return [vertex for vertex in self._adjacency_map.keys()]

    def edges(self, from_vertex: Vertex = None) -> list[Edge]:
        if from_vertex:
            if from_vertex in self._adjacency_map:
                return [edge for edge in self._adjacency_map[from_vertex]]
            else:
                raise ValueError
        else:
            return [edge for edges in self._adjacency_map.values() for edge in edges]
