from disjoint_set import DisjointSet

class Edge(object):
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


def kruskals(edges):
    """ Given a list of edges, determine the minimum spanning tree. 
    Requires each vertex of the edges to be initialized as a Disjoint set."""
    sorted_edges = sorted(edges, key=lambda x: x.weight)
    minimum_spanning_tree = set()
    for edge in sorted_edges:
        if edge.vertex1.find() != edge.vertex2.find():
            edge.vertex1.union(edge.vertex2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


def test_kruskals():
    # Initialize each vertex as a DisjointSet. These vertices will
    # have methods/attributes necessary for union/find functionality.
    a = DisjointSet('a')
    b = DisjointSet('b')
    c = DisjointSet('c')
    d = DisjointSet('d')

    # Initialize all edges with (vertex1, vertex2, weight)
    edge_1 = Edge(a, b, 1)
    edge_2 = Edge(a, c, 5)
    edge_3 = Edge(a, d, 3)
    edge_4 = Edge(b, c, 4)
    edge_5 = Edge(b, d, 2)
    edge_6 = Edge(c, d, 1)
    edges = [edge_1, edge_2, edge_3, edge_4, edge_5, edge_6]

    # Expected = {(A, B, 1), (C, D, 1), (B, D, 2)}
    expected_minimum_spanning_tree = set([edge_1, edge_5, edge_6])
    assert kruskals(edges) == expected_minimum_spanning_tree

