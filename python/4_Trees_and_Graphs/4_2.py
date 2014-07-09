"""
4.2

Given a directed graph, design an algorithm to find out whether there is
a route between two nodes.
"""
from classes import Stack, Queue, DirectedGraph

# Breadth First
def BFS(start, end):
    """
    Implemenents a queue to iteratively search for a path between two nodes.

    Visits all neighbors of current node, checks if any of them are end,
    and then adds them to the queue. Dequeues neighbors and puts them through
    the same process until the queue is empty.
    """
    assert start is not end, 'The nodes need to be different.'
    assert start is not None or end is not None, 'The nodes can\'t be None.'

    visited_set = set([start, end])
    bfs_queue = Queue(start)

    while bfs_queue.length > 0:
        start = bfs_queue.dq()
        for neighbor in start.neighbors:
            if neighbor is end:
                return True
            elif neighbor not in visited_set:
                visited_set.add(neighbor)
                bfs_queue.eq(neighbor)

