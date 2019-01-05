from node import Node
import lowest_common_ancestor
import pytest

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

test_data = [
    [root, 5, 1, 3],
    [root, 5, 4, 5]
]


@pytest.mark.parametrize('root,p,q,expected', test_data)
def test_lowest_common_ancestor_recursion(root, p, q, expected):
    assert lowest_common_ancestor.lowest_common_ancestor_recursion(
        root, p, q) == expected
