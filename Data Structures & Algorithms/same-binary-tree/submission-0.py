# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(node1,node2):
            if bool(node1) ^ bool(node2):
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            return traverse(node1.left,node2.left) and traverse(node1.right,node2.right)

        return traverse(p,q)
            