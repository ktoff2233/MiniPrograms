from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
                



if __name__ == "__main__":
    solution = Solution()
    nums1 = [0]
    result = solution.merge(nums1,0,[1],1)
    print(nums1)