# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTreeSlow(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return None
            node.left = invert(node.left)
            node.right = invert(node.right)
            node.right, node.left = node.left, node.right
            return node
        return invert(root)
    def invertTreeIter(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root

if __name__ == "__main__":
    solution = Solution()
    result = solution.invertTree("", "")
    print(result)