class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        prod = 1
        numGreaterThan = 0
        for j in range(1,len(nums)):
            prod *= nums[j]
            while i < j and prod >= k:
                prod /= nums[i]
                i += 1

            numGreaterThan += j - i + 1
        return numGreaterThan

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent([1,5,3,3,3,2,2,3,10], 2)
    print(result)