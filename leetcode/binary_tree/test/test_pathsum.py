from node import Node
import pathsum
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

root_c = Node(2)

root_d = Node(1)
root_d.left = Node(2)
root_d.left.left = Node(3)
root_d.left.left.left = Node(4)
root_d.left.left.left.right = Node(5)

test_data = [
    [root_a, 8, True],
    [root_b, 9, False],
    [root_c, 1, False],
    [root_d, 6, False]
]


@pytest.mark.parametrize('root,sum,expected', test_data)
def test_pathsum(root, sum, expected):
    assert pathsum.pathsum(root, sum) == expected
