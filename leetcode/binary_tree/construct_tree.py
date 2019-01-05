from node import Node


def construct_inorder_postorder(inorder, postorder):
    if not inorder or not postorder or len(inorder) != len(postorder) \
            or set(inorder) != set(postorder):
        return None
    if len(inorder) == 1:
        return Node(inorder[0])

    root = Node(postorder[-1])
    center_index = inorder.index(root.val)

    root.left = construct_inorder_postorder(
        inorder[:center_index], postorder[:center_index])
    root.right = construct_inorder_postorder(
        inorder[center_index+1:], postorder[center_index:len(postorder)-1])

    return root


def construct_inorder_preorder(inorder, preorder):
    if not inorder or not preorder or len(inorder) != len(preorder) \
            or set(inorder) != set(preorder):
        return None
    if len(inorder) == 1:
        return Node(inorder[0])

    root = Node(preorder[0])
    center_index = inorder.index(root.val)

    root.left = construct_inorder_preorder(
        inorder[:center_index], preorder[1:center_index+1])
    root.right = construct_inorder_preorder(
        inorder[center_index+1:], preorder[center_index+1:])

    return root
