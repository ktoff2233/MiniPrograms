from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(s)
        for i in count.values():
            if i > 1:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.isIsomorphic("", "")
    print(result)