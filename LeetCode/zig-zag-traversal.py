"""Write a function to print zig zag order traversal of a
binary tree. For the below binary tree.

Use two stacks:
currentLevel
nextLevel
a variable to keep track of the current level order

1. pop from current level stack and print the nodes value

1a. when the node is left to right, push the nodes left child
then its right child to the nextLevel stack
(loads in reverse order)

1b. when currentLevel is right to left, push nodes right child
first then left child 

2. Swap stacks at the end of each level (when currentLevel is empty)
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def zigZagTraversal(root):

    # Base case
    if root is None:

        # create the two stacks to store current and nextLevel
        currentLevel = []
        nextLevel = []

        # if ltr is true, push nodes from
        # left to right, otherwise, from
        # right to left
        ltr = True

        # append root to currentLevel stack
        currentLevel.append(root)

        # Check if stack is empty
        while len(currentLevel) > 0:
            # pop from stack
            tmp = currentLevel.pop(-1)
            # print the data
            print(tmp.data, " ", end='')

            if ltr:
                # if ltr is True, push left before right
                if tmp.left:
                    nextLevel.append(tmp.left)
                if tmp.right:
                    nextLevel.append(tmp.right)
            else:
                # else push right before left
                if tmp.right:
                    nextLevel.append(tmp.right)
                if tmp.left:
                    nextLevel.append(tmp.left)
            if len(currentLevel) == 0:
                # reverse ltr to push node in
                # opposite order
                ltr = not ltr
                # swapping of stacks
                currentLevel, nextLevel = nextLevel, currentLevel


if __name__ == '__main__':

    # build tree starting with root
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.right = Node(5)
    root.right.left = Node(4)

    print("Zig Zag Order of Binary Traversal is: ")
    zigZagTraversal(root)




