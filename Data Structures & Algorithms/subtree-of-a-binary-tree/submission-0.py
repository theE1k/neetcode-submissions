# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isSametree(node1,node2):
            if not node1 and not node2:
                return True
            if bool(node1) ^ bool(node2):
                return False
            if not isSametree(node1.left,node2.left) or not isSametree(node1.right,node2.right):
                return False
            return node1.val == node2.val
            
        if isSametree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)