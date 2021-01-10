class TreeNode:
    def __init__(self, x):
        """Initialize a tree node object which accepts an integer.
        """
        self.val = x
        self.left = None
        self.right = None


def invert_tree(node):
    """Recursively invert a tree by swapping the right and left nodes.

    Initially, the entire tree is accepted as a param, each recursion we go
    deeper down the trunk until finally we arrive at the end and go down the
    next branch. When there are no more branches, we finally return.
    """
    if node is None:
        return None

    node.left, node.right = node.right, node.left

    invert_tree(node.left)
    invert_tree(node.right)

    return node


def print_tree(node):
    """Print the output of the tree.
    """
    # Print the top level node
    print(node.val, end='')

    # If other nodes exist, print them too
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


def main():
    """Runs the program.
    """
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    print_tree(tree)
    print('')
    # Send the entire tree to be inverted
    inverted_tree = invert_tree(tree)
    print_tree(inverted_tree)
    return inverted_tree


if __name__ == '__main__':
    main()
