"""Given a tree and a node, the task is to find
the parent of the given node in the tree. Print -1
if the given node is the root node.

Write a recursive function that takes the current
node and its parent as the arguments (root node is passed with -1 as its parent).
If the current node is equal to the required node, then print
its parent and return else call the function recursively
for its children and the current node as the parent.
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findParent(node, val, parent):
    if node is None:
        return

    if node.data == val:
        print(parent)

    else:
        findParent(node.left, val, node.data)
        findParent(node.right, val, node.data)
