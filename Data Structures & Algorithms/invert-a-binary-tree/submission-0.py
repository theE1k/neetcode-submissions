# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(node):
        if not node: return
        traverse(node.left)
        traverse(node.right)    
        tmp = node.left
        node.left = node.right
        node.right = tmp
    
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        traverse(root)
        return root


    