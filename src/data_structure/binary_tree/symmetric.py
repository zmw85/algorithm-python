from src.data_structure.binary_tree.node import Node


def is_symmetric_iteration(root):
    if not root:
        return True

    children_left = [root.left]
    children_right = [root.right]

    while len(children_left) and len(children_right):
        def getvalue(node): return None if not node else node.val

        if list(map(getvalue, children_left)) \
                != list(map(getvalue, children_right)):
            return False
        children_right.reverse()

        temp = children_left
        children_left = []
        for node in temp:
            if node:
                children_left.append(node.left)
                children_left.append(node.right)

        temp = children_right
        children_right = []
        for node in temp:
            if node:
                children_right.insert(0, node.left)
                children_right.insert(0, node.right)

    return True
