# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def traverse(n,p,q):
            if not n:
                return None
            if n.val == p.val or n.val == q.val:
                return n
            left = traverse(n.left,p,q)
            right = traverse(n.right,p,q)
            if left and right:
                return n
            return left if left else right
        return traverse(root,p,q)