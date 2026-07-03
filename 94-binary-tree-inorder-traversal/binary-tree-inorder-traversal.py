# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def fun(node):
            if not node:
                return
            fun(node.left)
            res.append(node.val)
            fun(node.right)
        fun(root)
        return res
        