from src.data_structure.binary_tree.node import Node
from src.data_structure.binary_tree import construct_tree
from src.data_structure.binary_tree import serialization
import random
import pytest

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.right.right = Node(9)
root.right.left.left = Node(10)
root.right.right.left = Node(11)

inOrderResult = [8, 4, 2, 5, 9, 1, 10, 6, 3, 11, 7]
preOrderResult = [1, 2, 4, 8, 5, 9, 3, 6, 10, 7, 11]
postOrderResult = [8, 4, 9, 5, 2, 10, 6, 11, 7, 3, 1]


def test_construct_inorder_postorder():
    assert construct_tree.construct_inorder_postorder(
        inOrderResult, postOrderResult) == root


def test_construct_inorder_preorder():
    assert construct_tree.construct_inorder_preorder(
        inOrderResult, preOrderResult) == root


test_data = [
    [None, None],
    [[], None],
    # [random.shuffle(inOrderResult.copy()), inOrderResult],
    # [random.shuffle(inOrderResult.copy()), inOrderResult]
]


@pytest.mark.parametrize('root,expected', test_data)
def test_construct_inorder_random(root, expected):
    assert construct_tree.construct_inorder_random(root) == expected
