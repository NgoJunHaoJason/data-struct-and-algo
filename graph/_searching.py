from typing import Optional


from ._graph import DirectedGraph, Vertex


def breadth_first_search(
    directed_graph: DirectedGraph,
    start_vertex: Vertex,
    search_value: int,
) -> Optional[Vertex]:
    visited_vertices = set()
    vertices_to_visit = [start_vertex]

    while vertices_to_visit:
        vertex = vertices_to_visit.pop(0)

        if vertex.value == search_value:
            return vertex

        visited_vertices.add(vertex)

        vertices_to_visit.extend(
            [
                edge.to_vertex
                for edge in directed_graph.adjacency_map[vertex]
                if edge.to_vertex not in visited_vertices
            ]
        )

    return None


def depth_first_search(
    directed_graph: DirectedGraph,
    start_vertex: Vertex,
    search_value: int,
) -> Optional[Vertex]:
    visited_vertices = set()
    vertices_to_visit = [start_vertex]

    while vertices_to_visit:
        vertex = vertices_to_visit.pop(-1)

        if vertex.value == search_value:
            return vertex

        visited_vertices.add(vertex)

        neighbours = [
            edge.to_vertex
            for edge in directed_graph.adjacency_map[vertex]
            if edge.to_vertex not in visited_vertices
        ]
        neighbours.sort(key=lambda neighbour: neighbour.name)

        vertices_to_visit.extend(neighbours)

    return None
