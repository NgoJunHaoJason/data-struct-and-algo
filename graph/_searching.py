from ._graph import Graph
from ._vertex import Vertex


def breadth_first_search(
    graph: Graph,
    start_vertex: Vertex,
    search_value: int,
) -> Vertex | None:
    # use queue
    return _graph_search(graph, start_vertex, search_value, pop_index=0)


def depth_first_search(
    graph: Graph,
    start_vertex: Vertex,
    search_value: int,
) -> Vertex | None:
    # use stack
    return _graph_search(graph, start_vertex, search_value, pop_index=-1)


def _graph_search(
    graph: Graph,
    start_vertex: Vertex,
    search_value: int,
    pop_index: int,
) -> Vertex | None:
    visited_vertices = set()
    vertices_to_visit = [start_vertex]

    while vertices_to_visit:
        vertex = vertices_to_visit.pop(pop_index)

        if vertex.value == search_value:
            return vertex

        visited_vertices.add(vertex)

        unvisited_neighbours = [
            edge.to_vertex
            for edge in graph.edges(vertex)
            if edge.to_vertex not in visited_vertices
        ]
        unvisited_neighbours.sort(key=lambda neighbour: neighbour.key, reverse=True)

        vertices_to_visit.extend(unvisited_neighbours)

    return None
