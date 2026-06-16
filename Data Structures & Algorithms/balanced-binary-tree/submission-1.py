# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            if not node:
                return 0
            left_depth = traverse(node.left) 
            right_depth = traverse(node.right)
            if left_depth == -1: return -1
            if right_depth == -1: return -1
            if abs(left_depth - right_depth) > 1:
                return -1
            return max(left_depth,right_depth) + 1
        if not root: return True
        return False if traverse(root) == -1 else True