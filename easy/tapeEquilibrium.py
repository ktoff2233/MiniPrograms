from typing import List


class Solution:
    def equilibrium(self, input):
        total = sum(input)
        leftSum = 0
        minDiff = float("inf")
        for i in input:
            leftSum += i
            rightSum = total - leftSum
            diff = abs(leftSum - rightSum)
            minDiff = min(minDiff, diff)
        return minDiff

if __name__ == "__main__":
    solution = Solution()
    result = solution.equilibrium([3, 1, 2, 4, 3])
    print(result)

def solution(A,B):
    def count_pieces(length,stick1,stick2):
        return (stick1//length) + (stick2//length)
    def can_form_square(length,stick1,stick2):
        return count_pieces(length,stick1,stick2) >= 4
    for length in range(max(A,B),1,-1):
        if can_form_square(length,A,B):
            return length
    return 0
