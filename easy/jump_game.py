from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        out = 0
        for i in nums:
            if out < 0:
                return False
            elif out < i:
                out = i
            out -=1
        return True

    def canJumpGreedy(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0

if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,0,0]
    result = solution.canJump(nums1)
    print(result)