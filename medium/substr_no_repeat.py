class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        charMap = {}
        left = 0

        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLen = max(maxLen, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        return maxLen

if __name__ == "__main__":
    solution = Solution()
    input = " "
    result = solution.lengthOfLongestSubstring(input)
    print(result)