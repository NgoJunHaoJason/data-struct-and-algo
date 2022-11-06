from typing import Callable

import pytest

from ._edge import UnidirectionalEdge
from ._graph import DirectedGraph, Graph, UndirectedGraph
from ._searching import breadth_first_search, depth_first_search
from ._vertex import Vertex


@pytest.fixture
def vertices_and_edges_for_graph() -> tuple[set[Vertex], set[UnidirectionalEdge]]:
    vertex_a = Vertex("A", 3)
    vertex_b = Vertex("B", 2)
    vertex_c = Vertex("C", 1)
    vertex_d = Vertex("D", 1)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d}

    edge_ab = UnidirectionalEdge(vertex_a, vertex_b)
    edge_bb = UnidirectionalEdge(vertex_b, vertex_b)
    edge_bc = UnidirectionalEdge(vertex_b, vertex_c)
    edge_ad = UnidirectionalEdge(vertex_a, vertex_d)

    edges = {edge_ab, edge_bb, edge_bc, edge_ad}

    return vertices, edges


@pytest.fixture
def create_graph():
    def _create_graph(
        vertices: set[Vertex],
        edges: set[UnidirectionalEdge],
        is_directed: bool,
    ) -> Graph:
        return (
            DirectedGraph(vertices, edges)
            if is_directed
            else UndirectedGraph(vertices, edges)
        )

    yield _create_graph


@pytest.mark.parametrize("is_directed", [True, False])
def test_breadth_first_search(
    create_graph: Callable[[set[Vertex], set[UnidirectionalEdge], bool], Graph],
    is_directed: bool,
) -> None:
    vertex_a = Vertex("A", 3)
    vertex_b = Vertex("B", 2)
    vertex_c = Vertex("C", 1)
    vertex_d = Vertex("D", 1)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d}

    edge_ab = UnidirectionalEdge(vertex_a, vertex_b)
    edge_bb = UnidirectionalEdge(vertex_b, vertex_b)
    edge_bc = UnidirectionalEdge(vertex_b, vertex_c)
    edge_ad = UnidirectionalEdge(vertex_a, vertex_d)

    edges = {edge_ab, edge_bb, edge_bc, edge_ad}

    graph = create_graph(vertices, edges, is_directed)

    found_vertex = breadth_first_search(
        graph,
        start_vertex=vertex_a,
        search_value=1,
    )

    assert found_vertex is not None
    assert found_vertex == vertex_d


@pytest.mark.parametrize("is_directed", [True, False])
def test_depth_first_search(
    create_graph: Callable[[set[Vertex], set[UnidirectionalEdge], bool], Graph],
    is_directed: bool,
) -> None:
    vertex_a = Vertex("A", 3)
    vertex_b = Vertex("B", 2)
    vertex_c = Vertex("C", 1)
    vertex_d = Vertex("D", 1)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d}

    edge_ab = UnidirectionalEdge(vertex_a, vertex_b)
    edge_bb = UnidirectionalEdge(vertex_b, vertex_b)
    edge_bc = UnidirectionalEdge(vertex_b, vertex_c)
    edge_ad = UnidirectionalEdge(vertex_a, vertex_d)

    edges = {edge_ab, edge_bb, edge_bc, edge_ad}

    graph = create_graph(vertices, edges, is_directed)

    found_vertex = depth_first_search(
        graph,
        start_vertex=vertex_a,
        search_value=1,
    )

    assert found_vertex is not None
    assert found_vertex == vertex_c
