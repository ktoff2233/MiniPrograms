class Solution:
    def isPalindromeBrute(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        xStr = str(x)
        xRevStr = xStr[::-1]
        return xStr == xRevStr
    def isPalindromeEfficient(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        xStr = str(x)
        l,r = 0, len(xStr) - 1
        while l < r:
            if ord(xStr[l]) != ord(xStr[r]):
                return False
            l += 1
            r -= 1
        return True
    def isPalindromeEfficient2(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        div = 1
        while x>= 10 * div:
            div *= 10
        while x:
            if x // div != x% 10:
                return False
            x = (x % div) // 10
            div = div / 100
        return True
        

            
if __name__ == "__main__":
    sol = Solution()
    result = sol.isPalindromeEfficient2(121)
    print(result)
    