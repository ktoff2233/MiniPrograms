from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Example usage
    nums = [3,3]
    target = 6
    
    # Call the twoSum method and print the result
    result = solution.twoSumEfficient(nums, target)
    print(result)