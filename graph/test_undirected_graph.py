from ._edge import BidirectionalEdge
from ._undirected_graph import UndirectedGraph
from ._vertex import Vertex


def test_create_undirected_graph():
    vertex_a = Vertex("A", 2)
    vertex_b = Vertex("B", 3)
    vertex_c = Vertex("C", 5)
    vertex_d = Vertex("D", 7)
    vertex_e = Vertex("E", 11)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d, vertex_e}

    edge_ab = BidirectionalEdge(vertex_a, vertex_b)
    edge_bc = BidirectionalEdge(vertex_b, vertex_c)
    edge_ca = BidirectionalEdge(vertex_c, vertex_a)
    edge_cd = BidirectionalEdge(vertex_c, vertex_d)
    edge_be = BidirectionalEdge(vertex_b, vertex_e)

    edges = {edge_ab, edge_bc, edge_ca, edge_cd, edge_be}

    directed_graph = UndirectedGraph(vertices, edges)

    for vertex in vertices:
        assert vertex in directed_graph.adjacency_map

    for edge in edges:
        assert edge in directed_graph.adjacency_map[edge.vertex1]
        assert edge in directed_graph.adjacency_map[edge.vertex2]
