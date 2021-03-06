from src.data_structure.binary_tree.node import Node


def breadthfirst(root):
    result = []

    if not root:
        return result

    arr = [root]
    while len(arr):
        node = arr.pop(0)
        result.append(node.val)

        if node.left:
            arr.append(node.left)
        if node.right:
            arr.append(node.right)

    return result


def depthfirst_inorder_recursive(root, result=[]):
    if not root:
        return result

    if root.left:
        depthfirst_inorder_recursive(root.left, result)
    result.append(root.val)
    if root.right:
        depthfirst_inorder_recursive(root.right, result)

    return result


def depthfirst_inorder_stack(root):
    result = []
    if not root:
        return result

    stack = []
    node = root

    while node or len(stack):
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right

    return result


def depthfirst_preorder_recursive(root, result=[]):
    if not root:
        return result

    result.append(root.val)
    if root.left:
        depthfirst_preorder_recursive(root.left, result)
    if root.right:
        depthfirst_preorder_recursive(root.right, result)

    return result


def depthfirst_preorder_stack(root):
    result = []
    if not root:
        return result

    stack = [root]

    while len(stack):
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def depthfirst_postorder_recursive(root, result=[]):
    if not root:
        return result

    if root.left:
        depthfirst_postorder_recursive(root.left, result)
    if root.right:
        depthfirst_postorder_recursive(root.right, result)
    result.append(root.val)

    return result


def depthfirst_postorder_stack(root):
    result = []
    if not root:
        return result

    stack = []
    while True:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        print(stack[-1].val)
        root = stack.pop()

        if root.right and len(stack) and root.right == stack[-1]:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            result.append(root.val)
            root = None

        if len(stack) <= 0:
            break

    return result
