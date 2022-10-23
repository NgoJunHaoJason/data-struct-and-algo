from typing import Callable, Tuple
import pytest
from ._graph import DirectedGraph, Edge, Graph, UndirectedGraph, Vertex


def test_create_vertex() -> None:
    name = "A"
    value = 2
    vertex = Vertex(name, value)

    assert vertex.name == name
    assert vertex.value == value


def test_vertices_with_same_name_are_equal() -> None:
    name = "A"

    vertex1 = Vertex(name, value=2)
    vertex2 = Vertex(name, value=3)

    assert vertex1 == vertex2


def test_string_representation_of_vertex() -> None:
    name = "A"
    value = 2
    vertex = Vertex(name, value)

    assert str(vertex) == f"Vertex({name}: {value})"


def test_create_edge_with_default_weight() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge = Edge(vertex_a, vertex_b)

    assert edge.from_vertex == vertex_a
    assert edge.to_vertex == vertex_b
    assert edge.weight == 1


def test_edges_with_same_vertices_are_equal() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge1 = Edge(vertex_a, vertex_b, 5)
    edge2 = Edge(vertex_a, vertex_b, 7)
    edge3 = Edge(vertex_b, vertex_a, 11)

    assert edge1 == edge2
    assert edge1 != edge3


def test_string_representation_of_edge() -> None:
    name_a = "A"
    name_b = "B"
    weight = 5

    vertex_a = Vertex(name_a, 2)
    vertex_b = Vertex(name_b, 3)

    edge = Edge(vertex_a, vertex_b, weight)

    assert str(edge) == f"Edge({name_a} -{weight}-> {name_b})"


def test_get_edge_in_opposite_direction() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    original_edge = Edge(vertex_a, vertex_b, 5)
    opposite_edge = original_edge.opposite()

    assert opposite_edge.from_vertex == original_edge.to_vertex
    assert opposite_edge.to_vertex == original_edge.from_vertex
    assert opposite_edge.weight == original_edge.weight


@pytest.fixture
def vertices_and_edges_for_graph() -> Tuple[set[Vertex], set[Edge]]:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)
    vertex_c = Vertex("C", 5)
    vertex_d = Vertex("D", 7)
    vertex_e = Vertex("E", 11)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d, vertex_e}

    edge_ab = Edge(vertex_a, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    edge_ca = Edge(vertex_c, vertex_a)
    edge_cd = Edge(vertex_c, vertex_d)
    edge_be = Edge(vertex_b, vertex_e)

    edges = {edge_ab, edge_bc, edge_ca, edge_cd, edge_be}

    return vertices, edges


@pytest.fixture
def create_graph():
    def _create_graph(
        vertices: set[Vertex],
        edges: set[Edge],
        is_directed: bool,
    ) -> Graph:
        return (
            DirectedGraph(vertices, edges)
            if is_directed
            else UndirectedGraph(vertices, edges)
        )

    yield _create_graph


@pytest.mark.parametrize("is_directed", [True, False])
def test_correct_vertices_in_directed_graph(
    vertices_and_edges_for_graph: Tuple[set[Vertex], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, edges = vertices_and_edges_for_graph
    graph = create_graph(vertices, edges, is_directed)

    graph_vertices = graph.vertices()

    for vertex in vertices:
        assert vertex in graph_vertices

    for vertex in graph_vertices:
        assert vertex in vertices


@pytest.mark.parametrize("is_directed", [True, False])
def test_correct_edges_in_directed_graph(
    vertices_and_edges_for_graph: Tuple[set[Vertex], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, edges = vertices_and_edges_for_graph
    graph = create_graph(vertices, edges, is_directed)

    if not is_directed:
        opposite_edges = {
            Edge(edge.to_vertex, edge.from_vertex, edge.weight) for edge in edges
        }
        edges = edges.union(opposite_edges)

    graph_edges = graph.edges()

    for edge in edges:
        assert edge in graph_edges

    for edge in graph_edges:
        assert edge in edges


@pytest.mark.parametrize("is_directed", [True, False])
def test_get_neighbours_of_a_valid_vertex_in_a_directed_graph(
    vertices_and_edges_for_graph: Tuple[set[Vertex], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, edges = vertices_and_edges_for_graph
    graph = create_graph(vertices, edges, is_directed)

    for vertex in vertices:
        neighbours = graph.neighbours(vertex)

        for neighbour in neighbours:
            assert neighbour in vertices


@pytest.mark.parametrize("is_directed", [True, False])
def test_get_neighbours_of_an_invalid_vertex_in_a_directed_graph(
    vertices_and_edges_for_graph: Tuple[set[Vertex], set[Edge]],
    create_graph: Callable[[set[Vertex], set[Edge], bool], Graph],
    is_directed: bool,
) -> None:
    vertices, edges = vertices_and_edges_for_graph
    graph = create_graph(vertices, edges, is_directed)

    new_vertex = Vertex("Z", 0)
    with pytest.raises(ValueError):
        graph.neighbours(new_vertex)