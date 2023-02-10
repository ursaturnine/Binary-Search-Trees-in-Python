"""Check If Two Nodes are Cousins in a Binary Tree

Give the binary tree and the two nodes, say, 'a' and 'b', 
determine whether the two nodes are cousins of each other
or not.

Two nodes are cousins of each other if they are at the same
level and have different parents


Approach:
Find the level of one of the nodes. Using the found level, check
if 'a' and 'b'  are at this level. If 'a' and 'b' are at a given
level, then finally check if they are not children of some parent.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def areCousins(root, a, b):
    if root is None:
        return

    # find level using height of whole binary tree
    treeHeight = getTreeHeight(root)
    # find height of tree to a
    # find height of tree to b
    aNodeHeight = getTreeHeight(a)
    bNodeHeight = getTreeHeight(b)

    if (treeHeight - aNodeHeight) != (treeHeight-bNodeHeight):
        return False

    
    
    # find parent of b
    # check if they have same parents
    # if they are at same height and have different parents, return True

# returns a number
def getTreeHeight(node):
    if node is None:
        return
    return 1 + max(getTreeHeight(node.left), getTreeHeight(node.right))

