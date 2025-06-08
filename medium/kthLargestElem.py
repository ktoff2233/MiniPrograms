from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = heapq.nlargest(k, nums)
        return largest.pop(-1)
if __name__ == "__main__":
    solution = Solution()
    result = solution.findKthLargest([], 8)
    print(result)