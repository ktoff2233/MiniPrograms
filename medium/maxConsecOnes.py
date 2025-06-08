from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        countList = [0,0]
        maxOnes = 0
        i = 0
        for num in range(len(nums)):
            if nums[num] == 1:
                countList[0] += 1
            elif nums[num]  == 0 and countList[1] < k:
                countList[0] += 1
            if countList[1] >= k:
                maxOnes = max(maxOnes, countList[1])
                while i < num and countList[1] >= k:
                    if nums[i] == 1:
                        countList[0] -= 1
                    elif nums[i] == 0:
                        countList[1] -= 1
        return maxOnes

if __name__ == "__main__":
    solution = Solution()
    result = solution.findKthLargest([], 8)
    print(result)