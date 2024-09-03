from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in k:
            val = nums.pop()
            nums.insert(0,val)

    def rotateEfficient(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,4,5,6,7]
    result = solution.rotateAnother(nums1, 3)
   # print(nums1)