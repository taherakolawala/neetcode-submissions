# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(a, val):
            if a is None:
                return 0
            if a.val >= val:
                return 1 + good(a.left, a.val) + good(a.right, a.val)
            else:
                return good(a.left, val) + good(a.right, val)
        
        count = good(root, -10000)
        return count