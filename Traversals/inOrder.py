"""DFS: In order Traversal of Binary Tree.

(left, root, right)

1. Traverse the left subtree, i.e, call Inorder(left -> right)
2. Visit the root
3. Traverse the right subtree, i.e, call Inorder(right -> left)
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def inOrderTraversal(root):

    if root:

        inOrderTraversal(root.left)

        print(root.data)

        inOrderTraversal(root.right)

if __name__== '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('Inorder traversal of a binary tree is')
    inOrderTraversal(root)
