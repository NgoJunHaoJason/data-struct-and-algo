import math
from typing import Any, Optional, Tuple

from ._graph import Edge, UndirectedGraph, Vertex


def dijkstras_shortest_path(
    undirected_graph: UndirectedGraph,
    source_vertex: Vertex,
    destination_vertex: Vertex,
) -> Optional[Tuple[list[Edge], int]]:
    visited_vertices = {}
    vertices_to_visit = {
        source_vertex: {
            "shortest_distance": 0,
            "edge_leading_to_vertex": None,
        }
    }

    while vertices_to_visit:
        current_vertex = None
        shortest_distance = math.inf

        for vertex, info in vertices_to_visit.items():
            if info["shortest_distance"] < shortest_distance:
                current_vertex = vertex
                shortest_distance = info["shortest_distance"]

        visited_vertices[current_vertex] = vertices_to_visit.pop(current_vertex)

        if current_vertex == destination_vertex:
            edges_used = _get_edges_used(
                visited_vertices,
                source_vertex,
                destination_vertex,
            )
            return edges_used, shortest_distance

        for edge in undirected_graph._adjacency_map[current_vertex]:
            neighbour_vertex = edge.to_vertex

            if neighbour_vertex in visited_vertices:
                continue

            new_shortest_distance = shortest_distance + edge.weight

            if neighbour_vertex in vertices_to_visit:
                old_shortest_distance = vertices_to_visit[neighbour_vertex][
                    "shortest_distance"
                ]

                if new_shortest_distance >= old_shortest_distance:
                    continue

            info = {
                "shortest_distance": new_shortest_distance,
                "edge_leading_to_vertex": edge,
            }
            vertices_to_visit[neighbour_vertex] = info

    return None


def _get_edges_used(
    visited_vertices: dict[str, dict[str, Any]],
    source_vertex: Vertex,
    destination_vertex: Vertex,
) -> list[Edge]:
    visited_vertex = destination_vertex
    edges_used = []

    while visited_vertex != source_vertex:
        info = visited_vertices[visited_vertex]
        edge: Edge = info["edge_leading_to_vertex"]

        edges_used.insert(0, edge)
        visited_vertex = edge.from_vertex

    return edges_used
