from algorithms.search import BREADTH_DEPTH_FIRST_GRAPH
from algorithms.search.depth_first_search import depth_first_search


def test_depth_first_search():
    visited = set()
    traversal_order = []

    traversal_order = depth_first_search(visited, traversal_order, BREADTH_DEPTH_FIRST_GRAPH, 5)

    assert traversal_order == [5, 3, 2, 4, 8, 7]
