from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxReturn = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                maxReturn = max(maxReturn, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxReturn
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0]
    result = solution.merge(nums1,0,[1],1)
    print(nums1)