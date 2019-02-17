from src.data_structure.binary_tree.node import Node


def maxdepth_recursive(root):
    if not root:
        return 0

    max_left = maxdepth_recursive(root.left)
    max_right = maxdepth_recursive(root.right)
    return max_left + 1 if max_left > max_right else max_right + 1


def maxdepth_iteration(root):
    depth = 0

    if not root:
        return depth

    arr = [root]
    while len(arr):
        depth = depth + 1
        temp_arr = arr
        arr = []
        for node in temp_arr:
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)

    return depth
