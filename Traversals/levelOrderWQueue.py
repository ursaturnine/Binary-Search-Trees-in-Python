"""Given the root of the Binary Tree, print the level
order traversal of a tree. (Breadth-First Search)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelOrder(root):

    # Base Case
    if root is None:
        return 
    
    queue = []
    queue.append(root)

    while len(queue) > 0:
        # print front of queue then pop it
        print(queue[0].data, end = '')
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print('The level order traversal of the tree is :')
    printLevelOrder(root)