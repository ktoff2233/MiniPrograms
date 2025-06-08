class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while c != 0:
            bit1 = a&1
            bit2 = b&1
            bit3 = c&1
            a >>= 1
            b >>= 1
            c >>= 1
            if bit1 | bit2 == bit3:
                continue
            elif ~bit2 | bit1 == bit3:
                flips += 1
            elif ~bit1 | bit2 == bit3:
                flips += 1
            else:
                flips += 2
            print("bit3: " + str(bit3) + " curr: "  + str(c))

        return flips


if __name__ == "__main__":
    solution = Solution()
    result = solution.minFlips(2,6,5)
    print("minFlips: " + str(result))