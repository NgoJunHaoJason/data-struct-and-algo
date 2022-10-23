from ._graph import DirectedGraph, Edge, UndirectedGraph, Vertex


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


def test_create_edge_with_default_weight():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge = Edge(vertex_a, vertex_b)

    assert edge.from_vertex == vertex_a
    assert edge.to_vertex == vertex_b
    assert edge.weight == 1


def test_edges_with_same_vertices_are_equal():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    edge1 = Edge(vertex_a, vertex_b, 5)
    edge2 = Edge(vertex_a, vertex_b, 7)
    edge3 = Edge(vertex_b, vertex_a, 11)

    assert edge1 == edge2
    assert edge1 != edge3


def test_string_representation_of_edge():
    name_a = "A"
    name_b = "B"
    weight = 5

    vertex_a = Vertex(name_a, 2)
    vertex_b = Vertex(name_b, 3)

    edge = Edge(vertex_a, vertex_b, weight)

    assert str(edge) == f"Edge({name_a} -{weight}-> {name_b})"


def test_get_edge_in_opposite_direction():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)

    original_edge = Edge(vertex_a, vertex_b, 5)
    opposite_edge = original_edge.opposite()

    assert opposite_edge.from_vertex == original_edge.to_vertex
    assert opposite_edge.to_vertex == original_edge.from_vertex
    assert opposite_edge.weight == original_edge.weight


def test_create_directed_graph():
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

    directed_graph = DirectedGraph(vertices, edges)

    for vertex in vertices:
        assert vertex in directed_graph.adjacency_map

    for edge in edges:
        assert edge in directed_graph.adjacency_map[edge.from_vertex]


def test_create_undirected_graph():
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

    directed_graph = UndirectedGraph(vertices, edges)

    for vertex in vertices:
        assert vertex in directed_graph.adjacency_map

    for edge in edges:
        assert edge in directed_graph.adjacency_map[edge.from_vertex]

        opposite_edge = Edge(edge.to_vertex, edge.from_vertex, edge.weight)
        assert opposite_edge in directed_graph.adjacency_map[edge.to_vertex]
