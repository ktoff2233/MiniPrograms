from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,4,5,6,7]
    result = solution.rotateAnother(nums1, 3)
   # print(nums1)