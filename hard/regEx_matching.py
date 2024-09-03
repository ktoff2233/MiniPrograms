
#unfinished
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        loop = False
        for j in range(p):
            if j + 1 < len(p) and p[j + 1] == "*":
                pass
            while True:
                if p[j] != s[i] and p[j] != ".":
                    return False
                

        return i == len(s)


if __name__ == "__main__":
    solution = Solution()
    list1 = [1,2]
    list2 = [3,4]
    result = solution.findMedianSortedArraysEfficient(list1,list2)
    print(result)
