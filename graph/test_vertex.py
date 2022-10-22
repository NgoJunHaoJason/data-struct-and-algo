from ._vertex import Vertex


def test_create_vertex():
    name = "A"
    value = 2
    vertex = Vertex(name, value)

    assert vertex.name == name
    assert vertex.value == value


def test_vertices_with_same_name_are_equal():
    name = "A"

    vertex1 = Vertex(name, value=2)
    vertex2 = Vertex(name, value=3)

    assert vertex1 == vertex2


def test_string_representation_of_vertex():
    name = "A"
    value = 2
    vertex = Vertex(name, value)

    assert str(vertex) == f"Vertex({name}: {value})"
