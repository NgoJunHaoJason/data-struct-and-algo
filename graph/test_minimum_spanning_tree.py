import pytest

from ._edge import BidirectionalEdge
from ._graph import UndirectedGraph
from ._minimum_spanning_tree import prims_mst
from ._vertex import Vertex


@pytest.fixture
def graph_and_expected_edges() -> tuple[UndirectedGraph, set[BidirectionalEdge]]:
    vertex_a = Vertex("A", 0)
    vertex_b = Vertex("B", 0)
    vertex_c = Vertex("C", 0)
    vertex_d = Vertex("D", 0)
    vertex_e = Vertex("E", 0)
    vertex_f = Vertex("F", 0)

    vertices = {vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f}

    edge_ab = BidirectionalEdge(vertex_a, vertex_b, weight=2)
    edge_ac = BidirectionalEdge(vertex_a, vertex_c, weight=3)

    edge_bc = BidirectionalEdge(vertex_b, vertex_c, weight=5)
    edge_bd = BidirectionalEdge(vertex_b, vertex_d, weight=3)
    edge_be = BidirectionalEdge(vertex_b, vertex_e, weight=4)

    edge_ce = BidirectionalEdge(vertex_c, vertex_e, weight=4)

    edge_de = BidirectionalEdge(vertex_d, vertex_e, weight=2)
    edge_df = BidirectionalEdge(vertex_d, vertex_f, weight=3)

    edge_ef = BidirectionalEdge(vertex_e, vertex_f, weight=5)

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
    expected_edges = {edge_ab, edge_ac, edge_bd, edge_de, edge_df}

    return undirected_graph, expected_edges


def test_minimum_spanning_tree(
    graph_and_expected_edges: tuple[UndirectedGraph, set[BidirectionalEdge]]
) -> None:
    undirected_graph, expected_edges = graph_and_expected_edges

    minimum_spanning_tree: UndirectedGraph = prims_mst(undirected_graph)

    mst_edges = minimum_spanning_tree.edges()

    assert mst_edges == expected_edges

    actual_total_weight = sum(edge.weight for edge in mst_edges)
    expected_total_weight = sum(edge.weight for edge in expected_edges)

    assert actual_total_weight == expected_total_weight
