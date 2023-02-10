"""DFS: Preorder traversal is used to create a copy of the tree.
Preorder traversal is also used to get prefix expressions on an 
expression tree.
"""

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def preOrderTraversal(root):

    if root:

        print(root.val)

        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


# Driver code
if __name__== '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('Preorder traversal of a binary tree is')
    preOrderTraversal(root)