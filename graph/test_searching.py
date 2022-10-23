from ._graph import DirectedGraph, Edge, Vertex
from ._searching import breadth_first_search, depth_first_search


def test_breadth_first_search_return_nearest():
    vertex_a = Vertex("A", 3)
    vertex_b = Vertex("B", 2)
    vertex_c = Vertex("C", 1)
    vertex_d = Vertex("D", 1)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d}

    edge_ab = Edge(vertex_a, vertex_b)
    edge_ac = Edge(vertex_a, vertex_c)
    edge_bd = Edge(vertex_b, vertex_d)

    edges = {edge_ab, edge_ac, edge_bd}

    directed_graph = DirectedGraph(vertices, edges)

    found_vertex = breadth_first_search(
        directed_graph,
        start_vertex=vertex_a,
        search_value=1,
    )

    assert found_vertex is not None
    assert found_vertex == vertex_c


def test_depth_first_search_return_nearest():
    vertex_a = Vertex("A", 3)
    vertex_b = Vertex("B", 2)
    vertex_c = Vertex("C", 1)
    vertex_d = Vertex("D", 1)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d}

    edge_ab = Edge(vertex_a, vertex_b)
    edge_bb = Edge(vertex_b, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    edge_ad = Edge(vertex_a, vertex_d)

    edges = {edge_ab, edge_bb, edge_bc, edge_ad}

    directed_graph = DirectedGraph(vertices, edges)

    found_vertex = depth_first_search(
        directed_graph,
        start_vertex=vertex_a,
        search_value=1,
    )

    assert found_vertex is not None
    assert found_vertex == vertex_d
