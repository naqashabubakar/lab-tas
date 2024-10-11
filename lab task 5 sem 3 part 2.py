class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    None
    """
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.value, end=" ")
    inorder_traversal(root.right)

def preorder_traversal(root):
    """
    Performs a preorder traversal of a binary tree.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    None
    """
    if root is None:
        return

    print(root.value, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    """
    Performs a postorder traversal of a binary tree.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    None
    """
    if root is None:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value, end=" ")

def level_order_traversal(root):
    """
    Performs a level order traversal of a binary tree.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    None
    """
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Inorder traversal:")
inorder_traversal(root)
print("\nPreorder traversal:")
preorder_traversal(root)
print("\nPostorder traversal:")
postorder_traversal(root)
print("\nLevel order traversal:")
level_order_traversal(root)