from ._graph import Edge, UndirectedGraph, Vertex
from ._shortest_path import dijkstras_shortest_path


def test_dijkstras_algorithm():
    vertex_a = Vertex("A", 0)
    vertex_b = Vertex("B", 0)
    vertex_c = Vertex("C", 0)
    vertex_d = Vertex("D", 0)
    vertex_e = Vertex("E", 0)
    vertex_f = Vertex("F", 0)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f}

    edge_ab = Edge(vertex_a, vertex_b, weight=4)
    edge_ac = Edge(vertex_a, vertex_c, weight=2)

    edge_bc = Edge(vertex_b, vertex_c, weight=1)
    edge_bd = Edge(vertex_b, vertex_d, weight=5)

    edge_cd = Edge(vertex_c, vertex_d, weight=8)
    edge_ce = Edge(vertex_c, vertex_e, weight=10)

    edge_de = Edge(vertex_d, vertex_e, weight=2)
    edge_df = Edge(vertex_d, vertex_f, weight=6)

    edge_ef = Edge(vertex_e, vertex_f, weight=5)

    edges = {
        edge_ab,
        edge_ac,
        edge_bc,
        edge_bd,
        edge_cd,
        edge_ce,
        edge_de,
        edge_df,
        edge_ef,
    }

    undirected_graph = UndirectedGraph(vertices, edges)

    shortest_path = dijkstras_shortest_path(undirected_graph, vertex_a, vertex_f)

    assert shortest_path is not None

    edges_used, shortest_distance = shortest_path

    assert len(edges_used) == 4

    assert edges_used[0] == edge_ac
    assert edges_used[1] == edge_bc.opposite()
    assert edges_used[2] == edge_bd
    assert edges_used[3] == edge_df

    assert shortest_distance == 14
