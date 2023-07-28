class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_bst(preorder):
    if not preorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)

    i = 1
    while i < len(preorder) and preorder[i] < root_value:
        i += 1

    root.left = construct_bst(preorder[1:i])
    root.right = construct_bst(preorder[i:])

    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Test case 1
preorder1 = [10, 5, 1, 7, 40, 50]
root1 = construct_bst(preorder1)
print("Test case 1:")
print("Root:", root1.value)
print("Inorder Traversal:")
inorder_traversal(root1)
print()

# Test case 2
preorder2 = [40, 30, 20, 35, 55]
root2 = construct_bst(preorder2)
print("Test case 2:")
print("Root:", root2.value)
print("Inorder Traversal:")
inorder_traversal(root2)
print()
