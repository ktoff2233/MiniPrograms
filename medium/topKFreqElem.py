from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common(k)
        print(Counter(nums))
        mostCommon = []
        for i in count:
            mostCommon.append(i[0])
        return mostCommon

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent([1,5,3,3,3,2,2,3,10], 2)
    print(result)