from src.data_structure.binary_tree.node import Node


def lowest_common_ancestor_recursion(root, p, q):
    node = traverse_next(root, p, q)

    return node.val if node else None


def traverse_next(root, p, q):
    if not root:
        return None

    if root.val == p or root.val == q:
        return root

    left_found = traverse_next(root.left, p, q)
    right_found = traverse_next(root.right, p, q)

    if left_found and right_found:
        return root

    return left_found if left_found is not None else right_found


# def lowest_common_ancestor_iteration(root, p, q):
#     if not root:
#         return False

#     arr = [root]

#     while len(arr):
#         node = arr[0]
#         if node.right:
#             arr.insert(0, node.right)
#         if node.left:
#             arr.insert(0, node.left)
