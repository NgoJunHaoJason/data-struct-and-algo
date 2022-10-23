import math
import random

from ._graph import UndirectedGraph


def prims_mst(undirected_graph: UndirectedGraph) -> UndirectedGraph:
    vertices = undirected_graph.vertices()

    first_vertex = vertices[random.randrange(0, len(vertices))]
    visted_vertices = {first_vertex}

    first_edges = set(undirected_graph.edges(first_vertex))
    opposite_edges = {edge.opposite() for edge in first_edges}
    edges_to_consider = first_edges.union(opposite_edges)

    edges_used = set()

    while len(visted_vertices) < len(vertices) and edges_to_consider:
        shortest_edge = None
        lowest_cost = math.inf

        for edge in edges_to_consider:
            if edge.weight < lowest_cost and edge.to_vertex not in visted_vertices:
                shortest_edge = edge
                lowest_cost = edge.weight

        edges_used.add(shortest_edge)
        edges_used.add(shortest_edge.opposite())

        edges_to_consider.remove(shortest_edge)
        edges_to_consider.remove(shortest_edge.opposite())

        next_vertex = shortest_edge.to_vertex
        visted_vertices.add(next_vertex)

        next_edges = undirected_graph.edges(next_vertex)

        for edge in next_edges:
            if edge not in edges_used:
                edges_to_consider.add(edge)
                edges_to_consider.add(edge.opposite())

    return UndirectedGraph(set(vertices), edges_used)
