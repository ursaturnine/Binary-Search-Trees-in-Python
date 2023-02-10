"""Given a Binary Tree, traverse via post order traversal.

(left, right, root)

1. Traverse the left subtree, i.e, call postorder(left -> subtree)
2. Traverse the right subtree, i.e, call postorder(right -> subtree)
3. Visit the root
"""


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def postOrderTraversal(root):

    if root:

        postOrderTraversal(root.left)
        postOrderTraversal(root.right)

        print(root.val)

# Driver code
if __name__== '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('Postorder traversal of a binary tree is')
    postOrderTraversal(root)