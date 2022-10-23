from algorithms.search import BREADTH_DEPTH_FIRST_GRAPH
from algorithms.search.breadth_first_search import breadth_first_search


def test_breadth_first_search():
    visited = []

    traversal_order = breadth_first_search(visited, BREADTH_DEPTH_FIRST_GRAPH, 5)

    assert traversal_order == [5, 3, 7, 2, 4, 8]
