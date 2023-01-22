"""Given the root of a binary tree, return the inorder traversal of its nodes' values."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root:
            return self.traverse(root, [])
        
    def traverse(self, node, res):
        if node.left:
            self.traverse(node.left, res)
        
        res.append(node.val)
        
        
        if node.right:
            self.traverse(node.right, res )

        return res