from ._edge import BidirectionalEdge, UnidirectionalEdge
from ._vertex import Vertex


def test_create_unidirectional_edge_with_default_weight():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge = UnidirectionalEdge(vertex_a, vertex_b)

    assert edge.from_vertex == vertex_a
    assert edge.to_vertex == vertex_b
    assert edge.weight == 1


def test_unidirectional_edges_with_same_vertices_are_equal():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge1 = UnidirectionalEdge(vertex_a, vertex_b)
    edge2 = UnidirectionalEdge(vertex_a, vertex_b)
    edge3 = UnidirectionalEdge(vertex_b, vertex_a)

    assert edge1 == edge2
    assert edge1 != edge3


def test_string_representation_of_unidirectional_edge():
    name_a = "A"
    name_b = "B"
    weight = 5

    vertex_a = Vertex(name_a, 2)
    vertex_b = Vertex(name_b, 3)

    edge = UnidirectionalEdge(vertex_a, vertex_b, weight)

    assert str(edge) == f"Edge({name_a} --{weight}-> {name_b})"


def test_create_bidirectional_edge_with_default_weight():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge = BidirectionalEdge(vertex_a, vertex_b)

    assert edge.vertex1 == vertex_a
    assert edge.vertex2 == vertex_b
    assert edge.weight == 1


def test_unidirectional_edges_with_unordered_vertices_are_equal():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge1 = BidirectionalEdge(vertex_a, vertex_b)
    edge2 = BidirectionalEdge(vertex_a, vertex_b)
    edge3 = BidirectionalEdge(vertex_b, vertex_a)

    assert edge1 == edge2
    assert edge1 == edge3


def test_string_representation_of_bidirectional_edge():
    name_a = "A"
    name_b = "B"
    weight = 5

    vertex_a = Vertex(name_a, 2)
    vertex_b = Vertex(name_b, 3)

    edge = BidirectionalEdge(vertex_a, vertex_b, weight)

    assert str(edge) == f"Edge({name_a} --{weight}-- {name_b})"
