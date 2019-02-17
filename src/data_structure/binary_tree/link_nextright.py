from src.data_structure.binary_tree.node import Node


def link_nextright(root):
    if not root:
        return root

    arr = [root]
    while len(arr):
        for index in range(len(arr)):
            arr[index].next = arr[index + 1] if index + 1 < len(arr) else None

        new_arr = []
        for node in arr:
            if node.left:
                new_arr.append(node.left)
            if node.right:
                new_arr.append(node.right)
            arr = new_arr
