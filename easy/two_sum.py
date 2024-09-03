from typing import List
class Solution:
    def twoSumBrute(self,nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    def twoSumEfficient(self,nums: List[int], target: int) -> List[int]:
        n = len(nums)
        numsMap ={}

        for i in range(n):
            complement = target - nums[i]
            if complement in numsMap:
                return[i, numsMap[complement]]
            numsMap[nums[i]] = i
        return []

if __name__ == "__main__":
    solution = Solution()
    
    # Example usage
    nums = [3,3]
    target = 6
    
    # Call the twoSum method and print the result
    result = solution.twoSumEfficient(nums, target)
    print(result)