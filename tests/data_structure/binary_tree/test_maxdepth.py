from src.data_structure.binary_tree import maxdepth
from src.data_structure.binary_tree.node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


def test_maxdepth_recursive():
    assert maxdepth.maxdepth_recursive(root) == 3


def test_maxdepth_iteration():
    assert maxdepth.maxdepth_iteration(root) == 3
