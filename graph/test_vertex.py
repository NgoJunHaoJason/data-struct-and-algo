from ._vertex import Vertex


def test_create_vertex() -> None:
    key = "A"
    value = 2
    vertex = Vertex(key, value)

    assert vertex.key == key
    assert vertex.value == value


def test_vertices_with_same_key_are_equal() -> None:
    key = "A"

    vertex1 = Vertex(key, value=2)
    vertex2 = Vertex(key, value=3)

    assert vertex1 == vertex2


def test_string_representation_of_vertex() -> None:
    key = "A"
    value = 2
    vertex = Vertex(key, value)

    assert str(vertex) == f"Vertex({key}: {value})"
