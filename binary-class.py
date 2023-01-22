"""Binary Search Tree Class
Class Composition: Uses Node Class
insert()
delete()
get_min() -Recursive
get_max() -Recursive
in_order_traversal() -Recursive
remove()
"""

class Node:
    def __init__ (self, data, parent=None):
        self.data = data
        self.right = None
        self.left = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print(f'Self.root is {self.root.data}')
            return self.root
    
        return self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                return self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                print(f'Inserting node to the left {node.left.data}')
                return node.left
        else:
            if node.right:
                return self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                print(f'Inserting node to the right {node.right.data}')
                return node.right
    
    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    
    def get_min_value(self, node):
        if node.left:
            return self.get_min_value(node.left)
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    
    def get_max_value(self, node):
        if node.right:
            return self.get_max_value(node.right)
        return node.data
    
    
    def traverse(self):
        if self.root:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)
            
        print(node.data)


        if node.right:
            self.traverse_in_order(node.right)
    

    def remove(self, data):
        if self.root:
            return self.remove_node(data, self.root)
    
    def remove_node(self, data, node):
        # first, we find the node we want to remove
        if node is None:
            return
        
        if data < node.data:
                self.remove_node(data, node.left)
        elif data > node.data:
                self.remove_node(data, node.right)
        else:
            # we have found the node we want to delete, so we have to notify its parent

            # node to delete is LEAF node
            if node.left is None and node.right is None:
                print('Removing leaf node...%d' % node.data)
                parent = node.parent

                # node is to the left of its parent
                if parent is not None and parent.left == node:
                    parent.left = None
                
                # node is to the right of its parent
                if parent is not None and parent.right == node:
                    parent.right = None
                
                # node is the root node
                if parent is None:
                    self.root = None
                
                del node

            # node to delete has one child

            # node to delete has a right child
            elif node.left is None and node.right is not None:
                print('Removing a node with single right child...')
                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = node.right
                if parent is not None and parent.right == node:
                    parent.right = node.right

                # node is the root node    
                if parent is None:
                    self.root = node.right
                node.right.parent = parent

                del node
            
            # node to delete has a left child
            elif node.right is None and node.left is not None:
                print('Removing a node with a single left child...')
                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                
                else:
                    self.root = node.left
                node.left.parent = parent

                del node
            
            # node to delete has two children
            else:
                print('Removing node with two children...')
                predecessor = self.get_predecessor(node.left)

                # swap the node and the predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                # call function recursively; predecessor is a leaf node or has a single left child
                self.remove_node(data, predecessor)
        

        # largest item in the left-most sub-tree
    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
    
        return node










if __name__ == '__main__':
    bst = BinarySearchTree()
    print('Inserting...')
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)
    bst.insert(44)
    bst.insert(-12)
    bst.insert(19)
    bst.insert(22)

    print('Traversing....')
    bst.traverse()

    # remove root node
    bst.remove(44)

    print('Traversing after removal....')
    bst.traverse()

    print('Max value: %s' %bst.get_max())




        


    

