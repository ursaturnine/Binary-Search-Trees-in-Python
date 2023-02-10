"""Given a binary tree, the task is to print Level Order Traversal
of the Binary Tree in spiral form i.e, alternate order.

Nodes are traversed in alternate order from front to back.


1. Calculate the height of the tree
2. Recursively traverse each level
3. Print the level order traversal according to the current level.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# print spiral traversal of a tree
def levelOrderSpiral(root):
    h = getHeight(root)

    # if this variable is set, then the given level
    # is traversed from left to right
    ltr = False
    for i in range(1, h + 1):
        printGivenLevel(root, i, ltr)

        ltr = not ltr

# print nodes at a given level
def printGivenLevel(tree, level, ltr):
    if tree == None:
        return
    elif level == 1:
        print(tree.data, end='')
    elif level > 1:

        if ltr:
            printGivenLevel(tree.left, level - 1, ltr)
            printGivenLevel(tree.right, level - 1, ltr)
        else:
            printGivenLevel(tree.right, level - 1, ltr)
            printGivenLevel(tree.left, level - 1, ltr)


# get total tree height recursively
def getHeight(node):
    if node is None:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))


# driver code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

    levelOrderSpiral(root)






