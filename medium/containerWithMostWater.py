from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        l, r = 0, len(height) -1
        maxVol = -1
        maxHeight = max(height)
        while l < r:
            maxVol = max(maxVol, (r - l) * min(height[l], height[r]))
            if maxHeight * (r - l) <= maxVol:
                break

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxVol
        



if __name__ == "__main__":
    solution = Solution()
    
    result = solution.maxArea([1,8,6,2,5,4,8,3,7])
    print(result)
    