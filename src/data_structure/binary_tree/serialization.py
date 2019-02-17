from src.data_structure.binary_tree.node import Node


def serialize(root):
    result = []
    if not root:
        return result

    arr = [root]

    while len(arr):
        node = arr.pop(0)
        if node:
            result.append(node.val)
            arr = arr + [node.left, node.right]
        else:
            result.append(None)

    while result[-1] is None:
        result = result[0:len(result)-1]

    return result


def deserialize(serialized):
    root = None
    if not serialized or len(serialized) < 1:
        return root

    root = Node(serialized.pop(0))
    level_nodes = [root]

    while len(serialized):
        next_level_nodes = []
        for node in level_nodes:
            if len(serialized):
                val = serialized.pop(0)
                if val is not None:
                    node.left = Node(val)
                    next_level_nodes.append(node.left)
            if len(serialized):
                val = serialized.pop(0)
                if val is not None:
                    node.right = Node(val)
                    next_level_nodes.append(node.right)
        level_nodes = next_level_nodes

    return root
