from node import Node
import symmetric
import pytest

root_a = Node(1)
root_a.left = Node(2)
root_a.right = Node(3)
root_a.left.left = Node(4)
root_a.left.right = Node(5)
root_a.right.left = Node(6)

root_b = Node(1)
root_b.left = Node(2)
root_b.right = Node(2)
root_b.left.left = Node(3)
root_b.left.right = Node(4)
root_b.right.left = Node(4)
root_b.right.right = Node(3)

test_data = [
    [root_a, False],
    [root_b, True]
]


@pytest.mark.parametrize('root,expected', test_data)
def test_is_symmetric_iteration(root, expected):
    assert symmetric.is_symmetric_iteration(root) == expected
