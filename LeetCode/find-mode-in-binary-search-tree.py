"""Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        if not root:
            return
        
        stack = []
        node = root
        hash_map = {}
        max_val = float('-inf')
        res = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            hash_map[node.val] = hash_map.get(node.val, 0) + 1
            max_val = max(hash_map[node.val], max_val)
            node = node.right
        for key, value in hash_map.items():
            if value == max_val:
                res.append(key)
        return res