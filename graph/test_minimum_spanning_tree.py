from ._edge import Edge
from ._graph import UndirectedGraph
from ._minimum_spanning_tree import prims_mst
from ._vertex import Vertex


def test_minimum_spanning_tree():
    vertex_a = Vertex("A", 0)
    vertex_b = Vertex("B", 0)
    vertex_c = Vertex("C", 0)
    vertex_d = Vertex("D", 0)
    vertex_e = Vertex("E", 0)
    vertex_f = Vertex("F", 0)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f}

    edge_ab = Edge(vertex_a, vertex_b, weight=2)
    edge_ac = Edge(vertex_a, vertex_c, weight=3)

    edge_bc = Edge(vertex_b, vertex_c, weight=5)
    edge_bd = Edge(vertex_b, vertex_d, weight=3)
    edge_be = Edge(vertex_b, vertex_e, weight=4)

    edge_ce = Edge(vertex_c, vertex_e, weight=4)

    edge_de = Edge(vertex_d, vertex_e, weight=2)
    edge_df = Edge(vertex_d, vertex_f, weight=3)

    edge_ef = Edge(vertex_e, vertex_f, weight=5)

    edges = {
        edge_ab,
        edge_ac,
        edge_bc,
        edge_bd,
        edge_be,
        edge_ce,
        edge_de,
        edge_df,
        edge_ef,
    }

    undirected_graph = UndirectedGraph(vertices, edges)
    minimum_spanning_tree: UndirectedGraph = prims_mst(undirected_graph)

    mst_edges = set(minimum_spanning_tree.edges())

    expected_edges = {edge_ab, edge_ac, edge_bd, edge_de, edge_df}
    expected_edges = expected_edges.union({edge.opposite() for edge in expected_edges})

    assert mst_edges == expected_edges

    edge_weight_total = sum(edge.weight for edge in mst_edges) // 2
    assert edge_weight_total == 13
