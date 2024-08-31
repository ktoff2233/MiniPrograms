import math
class Solution:
    def reverseBrute(self, x: int) -> int:
        if x < 0:
            rev = int(str(int(x))[1:][::-1])
        else:
            rev = int(str(int(x))[::-1])
        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        
        return rev
    
    def reverseEfficient(self, x: int) -> int:
        MAX, MIN = 2 ** 31 -1,-(2 ** 31)
        
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if(res>MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if(res < MIN// 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res*10) + digit
        return res
            
        
if __name__ == "__main__":
    sol = Solution()
    result = sol.reverseEfficient(-123)
    print(result)