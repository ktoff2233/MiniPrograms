# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            if node.left and not node.right:
                return False
            if node.right and not node.left:
                return False
            if node.val < node.left.val or node.val > node.right.val:
                return False
            return dfs(node.left) and dfs(node.right)
if __name__ == "__main__":
    solution = Solution()
    result = solution.merge([1,5,3,3,3,2,2,3,10], 2)
    print(result)