import traversals
from node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


def test_breadthfirst():
    assert traversals.breadthfirst(
        root) == [1, 2, 3, 4, 5, 6]


result_inorder = [4, 2, 5, 1, 6, 3]
result_preorder = [1, 2, 4, 5, 3, 6]
result_postorder = [4, 5, 2, 6, 3, 1]


def test_depthfirst_inorder_recursive():
    assert traversals.depthfirst_inorder_recursive(
        root) == result_inorder


def test_depthfirst_inorder_stack():
    assert traversals.depthfirst_inorder_stack(
        root) == result_inorder


def test_depthfirst_preorder_recursive():
    assert traversals.depthfirst_preorder_recursive(
        root) == result_preorder


def test_depthfirst_preorder_stack():
    assert traversals.depthfirst_preorder_stack(
        root) == result_preorder


def test_depthfirst_postorder_recursive():
    assert traversals.depthfirst_postorder_recursive(
        root) == result_postorder


def test_depthfirst_postorder_stack():
    assert traversals.depthfirst_postorder_stack(
        root) == result_postorder
