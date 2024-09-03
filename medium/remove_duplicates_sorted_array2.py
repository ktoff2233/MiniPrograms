from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1,len(nums)):
            if i < 2 or nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i
    def removeDuplicatesEfficient(self, nums: List[int]) -> int:
        l = r = 0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            for i in range(min(2,count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0]
    result = solution.merge(nums1,0,[1],1)
print(nums1)