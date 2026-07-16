# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower = min(p.val, q.val)
        higher = max(p.val, q.val)
        if lower <= root.val and higher >= root.val:
            return root
        if lower > root.val and higher > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if lower < root.val and higher < root.val:
            return self.lowestCommonAncestor(root.left, p, q)