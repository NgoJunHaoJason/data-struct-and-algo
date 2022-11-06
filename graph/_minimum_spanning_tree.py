import math
import random

from ._edge import BidirectionalEdge
from ._graph import UndirectedGraph
from ._vertex import Vertex


def prims_mst(undirected_graph: UndirectedGraph) -> UndirectedGraph:
    vertices = list(undirected_graph.vertices())

    first_vertex = vertices[random.randrange(0, len(vertices))]
    visited_vertices = {first_vertex}

    edges_to_consider = undirected_graph.edges(first_vertex)
    edges_used = set()

    while len(visited_vertices) < len(vertices) and edges_to_consider:
        shortest_edge = _get_shortest_edge(edges_to_consider, visited_vertices)

        edges_used.add(shortest_edge)
        edges_to_consider.remove(shortest_edge)

        next_vertex = (
            shortest_edge.vertex1
            if shortest_edge.vertex2 in visited_vertices
            else shortest_edge.vertex2
        )
        visited_vertices.add(next_vertex)

        next_edges = undirected_graph.edges(next_vertex)

        for edge in next_edges:
            if edge not in edges_used:
                edges_to_consider.add(edge)

    return UndirectedGraph(set(vertices), edges_used)


def _get_shortest_edge(
    edges_to_consider: set[BidirectionalEdge],
    visted_vertices: set[Vertex],
) -> BidirectionalEdge:
    shortest_edge = None
    lowest_cost = math.inf

    for edge in edges_to_consider:
        if edge.weight < lowest_cost and (
            edge.vertex1 not in visted_vertices or edge.vertex2 not in visted_vertices
        ):
            shortest_edge = edge
            lowest_cost = edge.weight

    return shortest_edge
