class Solution:

    def isBalanced(self, root):
            if root is None:
                return True
            return self.isBalanced(root.right) and self.isBalanced(root.left) and abs(self.get_height(root.left) - self.get_height(root.right)) <=1

        
    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
