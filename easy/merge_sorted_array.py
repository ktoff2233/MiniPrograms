from typing import List
class Solution:
    """
        in-place modification of nums1.
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k = m-1,n-1,n+m-1
        while j >= 0:
            if i >=0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0]
    result = solution.merge(nums1,0,[1],1)
    print(nums1)