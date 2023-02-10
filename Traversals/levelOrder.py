"""Given the root of the Binary Tree, print the level
order traversal of a tree. (Breadth-First Search)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

# print level order traversal of a tree
def levelOrderTraversal(root):
    h = getHeight(root)

    for i in range(1, h + 1):
        printCurrentLevel(root, i)

# print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return 
    if level == 1:
        print(root.data, " ", end='')
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level -1)



# get height
def getHeight(node):
    if node == None:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))
    

