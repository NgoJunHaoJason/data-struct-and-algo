import pytest

from typing import Callable

from ._edge import BidirectionalEdge, Edge, UnidirectionalEdge
from ._graph import DirectedGraph, Graph, UndirectedGraph
from ._vertex import Vertex


@pytest.fixture
def vertices_and_vertex_pairs() -> tuple[set[Vertex], set[tuple[Vertex]]]:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)
    vertex_c = Vertex("C", 5)
    vertex_d = Vertex("D", 7)
    vertex_e = Vertex("E", 11)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d, vertex_e}

    vertex_pairs = {
        (vertex_a, vertex_b),
        (vertex_b, vertex_c),
        (vertex_c, vertex_a),
        (vertex_c, vertex_d),
        (vertex_b, vertex_e),
    }

    return vertices, vertex_pairs


@pytest.fixture
def create_edges():
    def _create_edges(vertex_pairs: set[tuple[Vertex]], is_directed: bool) -> set[Edge]:
        if is_directed:
            return {
                UnidirectionalEdge(vertex1, vertex2)
                for vertex1, vertex2 in vertex_pairs
            }
        else:
            return {
                BidirectionalEdge(vertex1, vertex2) for vertex1, vertex2 in vertex_pairs
            }

    yield _create_edges


@pytest.fixture
def create_graph():
    def _create_graph(
        vertices: set[Vertex], edges: set[Edge], is_directed: bool
    ) -> Graph:
        return (
            DirectedGraph(vertices, edges)
            if is_directed
            else UndirectedGraph(vertices, edges)
        )

    yield _create_graph


@pytest.mark.parametrize("is_directed", [True, False])
def test_valid_vertices_in_graph(
    vertices_and_vertex_pairs: tuple[set[Vertex], set[tuple[Vertex]]],
    create_edges: Callable[[set[tuple[Vertex]], bool], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, vertex_pairs = vertices_and_vertex_pairs
    edges = create_edges(vertex_pairs, is_directed)
    graph = create_graph(vertices, edges, is_directed)

    graph_vertices = graph.vertices()

    for vertex in vertices:
        assert vertex in graph_vertices

    for vertex in graph_vertices:
        assert vertex in vertices


@pytest.mark.parametrize("is_directed", [True, False])
def test_valid_edges_in_graph(
    vertices_and_vertex_pairs: tuple[set[Vertex], set[tuple[Vertex]]],
    create_edges: Callable[[set[tuple[Vertex]], bool], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, vertex_pairs = vertices_and_vertex_pairs
    edges = create_edges(vertex_pairs, is_directed)
    graph = create_graph(vertices, edges, is_directed)

    graph_edges = graph.edges()

    for edge in edges:
        assert edge in graph_edges

    for edge in graph_edges:
        assert edge in edges


@pytest.mark.parametrize("is_directed", [True, False])
def test_valid_edges_from_a_valid_vertex_in_graph(
    vertices_and_vertex_pairs: tuple[set[Vertex], set[tuple[Vertex]]],
    create_edges: Callable[[set[tuple[Vertex]], bool], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, vertex_pairs = vertices_and_vertex_pairs
    edges = create_edges(vertex_pairs, is_directed)
    graph = create_graph(vertices, edges, is_directed)

    for vertex in vertices:
        graph_edges = graph.edges(vertex)

        for edge in graph_edges:
            assert edge in edges


@pytest.mark.parametrize("is_directed", [True, False])
def test_edges_from_an_invalid_vertex_in_graph(
    vertices_and_vertex_pairs: tuple[set[Vertex], set[tuple[Vertex]]],
    create_edges: Callable[[set[tuple[Vertex]], bool], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, vertex_pairs = vertices_and_vertex_pairs
    edges = create_edges(vertex_pairs, is_directed)
    graph = create_graph(vertices, edges, is_directed)

    new_vertex = Vertex("Z", 0)
    with pytest.raises(ValueError):
        graph.edges(new_vertex)
