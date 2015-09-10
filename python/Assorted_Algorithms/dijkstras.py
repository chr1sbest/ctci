from sys import maxint
from heapq import heappush, heappop

class Vertex(object):
    def __init__(self, node):
        self.id = node
        self.adjacent_nodes = {}
        self.visited = False
        self.distance = maxint

    def reset(self):
        self.visited = False
        self.distance = maxint


def dijkstras(starting_node, ending_node):
    # Initialize distance to starting node as 0 and initialize min heap
    starting_node.distance = 0
    minheap = [(0, starting_node)]
    while minheap:
        distance_to_current, current_node = heappop(minheap)
        current_node.visited = True
        # Iterate through each adjacent node to update distances.
        for vertex, distance in current_node.adjacent_nodes.items():
            # Skip vertexes that have already been visited.
            if vertex.visited == True:
                continue
            # Update distance to this vertex if it's less than prev
            new_distance = distance_to_current + distance
            if new_distance < vertex.distance:
                vertex.distance = new_distance 
            # Add this vertex to the min heap to eventually visit
            heappush(minheap, (new_distance, vertex))
    # When minheap is empty, all reachable nodes have been processed
    return ending_node.distance


def test_dijkstras():
    # Initialize vertices with distance (maxint), visited = False
    vertex_s = Vertex('s')
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_c = Vertex('c')
    vertex_d = Vertex('d')
    vertex_t = Vertex('t')
    # Set adjacent nodes
    vertex_s.adjacent_nodes = {vertex_a: 2, vertex_b: 1}
    vertex_a.adjacent_nodes = {vertex_s: 3, vertex_b: 4, vertex_c:8}
    vertex_b.adjacent_nodes = {vertex_s: 4, vertex_a: 2, vertex_d: 2}
    vertex_c.adjacent_nodes = {vertex_a: 2, vertex_d: 7, vertex_t: 4}
    vertex_d.adjacent_nodes = {vertex_b: 1, vertex_c: 11, vertex_t: 5}
    vertex_t.adjacent_nodes = {vertex_c: 3, vertex_d: 5}

    # s -> b -> d = 3
    shortest_from_s_to_d = dijkstras(vertex_s, vertex_d)
    assert shortest_from_s_to_d == 3

    # Reset distance and visited value for all vertices
    for vertex in [vertex_s, vertex_a, vertex_b, vertex_c, vertex_d, vertex_t]:
        vertex.reset()

    # d -> c = 11  ||  d -> t -> c = 8
    shortest_from_d_to_c = dijkstras(vertex_d, vertex_c)
    assert shortest_from_d_to_c == 8
