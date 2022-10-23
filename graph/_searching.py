from typing import Optional


from ._graph import Graph, Vertex


def breadth_first_search(
    graph: Graph,
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

        unvisited_neighbours = [
            neighbour
            for neighbour in graph.neighbours(vertex)
            if neighbour not in visited_vertices
        ]
        vertices_to_visit.extend(unvisited_neighbours)

    return None


def depth_first_search(
    graph: Graph,
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

        unvisited_neighbours = [
            neighbour
            for neighbour in graph.neighbours(vertex)
            if neighbour not in visited_vertices
        ]
        unvisited_neighbours.sort(key=lambda neighbour: neighbour.name, reverse=True)

        vertices_to_visit.extend(unvisited_neighbours)

    return None
