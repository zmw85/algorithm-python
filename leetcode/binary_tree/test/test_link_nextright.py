from node import TreeLinkNode
import link_nextright

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.right.left = TreeLinkNode(5)
root.right.right = TreeLinkNode(6)

expectedRoot = TreeLinkNode(1)
expectedRoot.left = TreeLinkNode(2)
expectedRoot.right = TreeLinkNode(3)
expectedRoot.left.left = TreeLinkNode(4)
expectedRoot.right.left = TreeLinkNode(5)
expectedRoot.right.right = TreeLinkNode(6)
expectedRoot.left.next = expectedRoot.right
expectedRoot.left.left.next = expectedRoot.right.left
expectedRoot.right.left.next = expectedRoot.right.right


def test_link_nextright():
    link_nextright.link_nextright(root)
    assert root == expectedRoot
