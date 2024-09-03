from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[total] = nums[i]
                index += 1
        return index 

   
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0]
    result = solution.merge(nums1,0,[1],1)
    print(nums1)