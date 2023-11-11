# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            child_queue = deque()
            prev = -1
            while queue:
                current = queue.popleft()
                if current.left:
                    child_queue.append(current.left)
                if current.right:
                    child_queue.append(current.right)
            prev = current
            result.append(prev.val)
            queue = child_queue
        return result