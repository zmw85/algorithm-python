from src.data_structure.binary_tree.node import Node


def pathsum(root, total, sum=0):
    if not root:
        return sum == total

    if not root.left and not root.right:
        return total == sum + root.val
    else:
        left = pathsum(root.left, total, sum +
                       root.val) if root.left else False
        right = pathsum(root.right, total, sum +
                        root.val) if root.right else False
        return left or right
