class Node:
    'Tree node class'

    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __eq__(self, other):
        return other and isinstance(other, Node) and self.left == other.left \
            and self.right == other.right and self.val == other.val

    def __ne__(self, other):
        return not __eq__(self, other)


class TreeLinkNode(Node):
    'Tree node class with next right child'

    def __init__(self, val):
        super(TreeLinkNode, self).__init__(val)
        self.next = None

    def __eq__(self, other):
        return super.__eq__(self, other) and self.next == other.next

    def __ne__(self, other):
        return not __eq__(self, other)
