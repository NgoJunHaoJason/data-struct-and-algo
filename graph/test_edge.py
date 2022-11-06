from ._edge import UnidirectionalEdge, BidirectionalEdge
from ._vertex import Vertex


def test_create_unidirectional_edge_with_default_weight() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge = UnidirectionalEdge(vertex_a, vertex_b)

    assert edge.vertex1 == vertex_a
    assert edge.vertex2 == vertex_b
    assert edge.weight == 1


def test_equality_of_unidirectional_edges() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge1 = UnidirectionalEdge(vertex_a, vertex_b, 5)
    edge2 = UnidirectionalEdge(vertex_a, vertex_b, 7)
    edge3 = UnidirectionalEdge(vertex_b, vertex_a, 11)

    assert edge1 == edge2
    assert edge1 != edge3


def test_string_representation_of_unidirectional_edge() -> None:
    key_a = "A"
    key_b = "B"
    weight = 5

    vertex_a = Vertex(key_a, 2)
    vertex_b = Vertex(key_b, 3)

    edge = UnidirectionalEdge(vertex_a, vertex_b, weight)

    assert str(edge) == f"UnidirectionalEdge({key_a} --{weight}-> {key_b})"


def test_get_unidirectional_edge_in_opposite_direction() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    original_edge = UnidirectionalEdge(vertex_a, vertex_b, 5)
    opposite_edge = original_edge.opposite()

    assert opposite_edge.vertex1 == original_edge.vertex2
    assert opposite_edge.vertex2 == original_edge.vertex1
    assert opposite_edge.weight == original_edge.weight


def test_create_bidirectional_edge_with_default_weight() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge = BidirectionalEdge(vertex_a, vertex_b)

    assert edge.vertex1 == vertex_a
    assert edge.vertex2 == vertex_b
    assert edge.weight == 1


def test_equality_of_bidirectional_edges() -> None:
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge1 = BidirectionalEdge(vertex_a, vertex_b, 5)
    edge2 = BidirectionalEdge(vertex_a, vertex_b, 7)
    edge3 = BidirectionalEdge(vertex_b, vertex_a, 11)

    assert edge1 == edge2
    assert edge1 == edge3


def test_string_representation_of_unidirectional_edge() -> None:
    key_a = "A"
    key_b = "B"
    weight = 5

    vertex_a = Vertex(key_a, 2)
    vertex_b = Vertex(key_b, 3)

    edge = BidirectionalEdge(vertex_a, vertex_b, weight)

    assert str(edge) == f"BidirectionalEdge({key_a} --{weight}-- {key_b})"
