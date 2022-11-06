from __future__ import annotations
from abc import ABC, abstractmethod

from ._edge import BidirectionalEdge, UnidirectionalEdge
from ._vertex import Vertex


class Graph(ABC):
    @abstractmethod
    def vertices(self) -> set[Vertex]:
        raise NotImplementedError

    @abstractmethod
    def edges(self, vertex: Vertex = None) -> set[UnidirectionalEdge]:
        raise NotImplementedError


class DirectedGraph(Graph):
    def __init__(self, vertices: set[Vertex], edges: set[UnidirectionalEdge]) -> None:
        self._adjacency_map: dict[Vertex, list[UnidirectionalEdge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self._adjacency_map[edge.vertex1].append(edge)

    def vertices(self) -> set[Vertex]:
        return {vertex for vertex in self._adjacency_map.keys()}

    def edges(self, vertex: Vertex = None) -> set[UnidirectionalEdge]:
        if vertex:
            if vertex in self._adjacency_map:
                return {edge for edge in self._adjacency_map[vertex]}
            else:
                raise ValueError
        else:
            return {edge for edges in self._adjacency_map.values() for edge in edges}


class UndirectedGraph(Graph):
    def __init__(self, vertices: set[Vertex], edges: set[BidirectionalEdge]) -> None:
        self._adjacency_map: dict[Vertex, list[BidirectionalEdge]] = {
            vertex: [] for vertex in vertices
        }

        for edge in edges:
            self._adjacency_map[edge.vertex1].append(edge)
            self._adjacency_map[edge.vertex2].append(edge)

    def vertices(self) -> set[Vertex]:
        return {vertex for vertex in self._adjacency_map.keys()}

    def edges(self, vertex: Vertex = None) -> set[BidirectionalEdge]:
        if vertex:
            if vertex in self._adjacency_map:
                return {edge for edge in self._adjacency_map[vertex]}
            else:
                raise ValueError
        else:
            return {edge for edges in self._adjacency_map.values() for edge in edges}
