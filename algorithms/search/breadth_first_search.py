from . import BREADTH_DEPTH_FIRST_GRAPH


def main():
    visited = []

    traversal_order = breadth_first_search(visited, BREADTH_DEPTH_FIRST_GRAPH, 5)

    print(traversal_order)


def breadth_first_search(visited, graph, node):
    """Searches the entirety of neighbors before traversing down."""
    queue = []
    traversal_order = []

    # Setup the initial node
    visited.append(node)
    queue.append(node)

    # While we have nodes to work through, keep traversing
    while queue:
        member = queue.pop(0)
        traversal_order.append(member)

        for neighbor in graph[member]:
            if neighbor not in visited:
                visited.append(neighbor)  # mark this node as visited
                queue.append(neighbor)  # queue up the neighbor to be traversed

    return traversal_order


if __name__ == '__main__':
    main()
