from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS -1
        while l <= r:
            row = (l + r)//2
            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row -1
            else:
                break
        if not (l <= r):
            return False
        row = (l+r)//2
        l,r = 0,COLS-1
        while l <= r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False



if __name__ == "__main__":
    solution = Solution()
    result = solution.searchMatrix("", "")
    print(result)