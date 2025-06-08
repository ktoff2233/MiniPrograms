from typing import List
class Solution:
    def jump(self, nums: List[int]) -> bool:
        res = l = r = 0
        while r < len(nums) -1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1
        return res
        
        

            

if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,0,0]
    result = solution.canJump(nums1)
    print(result)