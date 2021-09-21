from algorithms.recursion.invert_binary_tree import main


def test_run_invert_tree():
    tree = main()

    assert tree.val == 1
    assert tree.left.val == 3
    assert tree.left.right.val == 6
    assert tree.left.left.val == 7
    assert tree.right.val == 2
    assert tree.right.right.val == 4
    assert tree.right.left.val == 5
