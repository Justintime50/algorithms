from . import BREADTH_DEPTH_FIRST_GRAPH


def main():
    visited = {}
    traversal_order = []

    output = depth_first_search(visited, traversal_order, BREADTH_DEPTH_FIRST_GRAPH, 5)

    print(output)


def depth_first_search(visited, traversal_order, graph, node):
    """Searches the entirety of a single branch before backtracking to traverse a neighbor."""
    if node not in visited:
        traversal_order.append(node)  # only for testing/output purposes and not part of the algorithm
        visited.add(node)

        for neighbor in graph[node]:
            depth_first_search(visited, traversal_order, graph, neighbor)

    return traversal_order


if __name__ == "__main__":
    main()
