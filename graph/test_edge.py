from ._edge import Edge
from ._vertex import Vertex


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
    key_a = "A"
    key_b = "B"
    weight = 5

    vertex_a = Vertex(key_a, 2)
    vertex_b = Vertex(key_b, 3)

    edge = Edge(vertex_a, vertex_b, weight)

    assert str(edge) == f"Edge({key_a} --{weight}-> {key_b})"


def test_get_edge_in_opposite_direction() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    original_edge = Edge(vertex_a, vertex_b, 5)
    opposite_edge = original_edge.opposite()

    assert opposite_edge.from_vertex == original_edge.to_vertex
    assert opposite_edge.to_vertex == original_edge.from_vertex
    assert opposite_edge.weight == original_edge.weight
