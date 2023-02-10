"""Use Level Order Traversal in reverse given a Binary Tree! 
Print nodes from left to right.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Recursively
def printReverseOrder(root):
    h = getHeight(root)

    for i in reversed(range(1, h +1)):
        printLevelsReversed(root, i)


def printLevelsReversed(root, level):
    # Base Case
    if root is None:
        return
    
    if level == 1:
        print(root.data, ' ', end='')
    elif level > 1:
        printLevelsReversed(root.left, level -1)
        printLevelsReversed(root.right, level -1)

# Get height; iterative
def getHeight(node):
    if node is None:
        return 0
    
    lheight = getHeight(node.left)
    rheight = getHeight(node.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


# Driver code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print('The level order traversal of the tree is :')
    printReverseOrder(root)


