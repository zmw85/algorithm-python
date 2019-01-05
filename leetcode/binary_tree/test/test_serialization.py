from node import Node
import serialization

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

serialized = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]


def test_serialize():
    assert serialization.serialize(root) == serialized


def test_deserialize():
    assert serialization.deserialize(serialized) == root
