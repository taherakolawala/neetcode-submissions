# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            res.append(q[0].val)
            for _ in range(len(q)):
                if q[0].right:
                    q.append(q[0].right)
                if q[0].left:
                    q.append(q[0].left)
                q.popleft()
        return res